import json
import re
from typing import Dict, Any

from fastapi import Request, Response, Cookie, Depends

import jwt
from datetime import datetime, timedelta, timezone
import uuid

import errors
from models.user import User, UserSession, Admin
from schemas.auth import Refresh
from db import Session, get_database
from settings import settings


agent_parse = re.compile(r"^([\w]*)\/([\d\.]*)\s*(\((.*?)\)\s*(.*))?$")


def set_cookie(access: str, response: Response, max_age: int):
    response.set_cookie("access", access, httponly=True, samesite="lax", max_age=max_age)
    # response.set_cookie("access", access)


def get_user_agent_info(request: Request):
    ip = request.client[0]
    user_agent = request.headers.get("user-agent")
    # TODO: Rewrite select only client IP from headers
    if "X-Forwarded-For" in request.headers:
        info = [request.headers["X-Forwarded-For"]]
    elif "Forwarded" in request.headers:
        info = [request.headers["Forwarded"]]
    else:
        info = [ip]
    match = agent_parse.fullmatch(user_agent)
    if match:
        info += list(match.groups())
    return "".join(json.dumps(info, ensure_ascii=False, separators=(",", ":")))


def encode_token(payload) -> str:
    return jwt.encode(payload, settings.JWT_SECRET, algorithm='HS256')


def decode_token(token: str, token_type: str, suppress: bool = False) -> Dict[str, Any]:
    try:
        data = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'],
                          options={"require": ["exp", "role", "session", "type", "identity"]})
        if data["role"] != token_type:
            raise errors.token_validation_failed()
        return data
    except jwt.ExpiredSignatureError:
        if suppress:
            data = jwt.decode(token, settings.JWT_SECRET, algorithms=['HS256'],
                              options={"verify_signature": False})
            if data["role"] != token_type:
                raise errors.token_validation_failed()
            return data
        raise errors.token_expired()
    except jwt.DecodeError:
        raise errors.token_validation_failed()


def init_user_tokens(user: User, long: bool, request: Request, response: Response, db: Session) -> Refresh:
    now = datetime.now(timezone.utc)
    identity = f"{uuid.uuid1(int(now.timestamp()))}"
    session = UserSession()
    session.user = user
    session.fingerprint = get_user_agent_info(request)
    session.identity = identity
    if long:
        session.invalid_after = now + timedelta(hours=settings.JWT_REFRESH_LONG_EXPIRE)
        max_age = settings.JWT_REFRESH_LONG_EXPIRE * 3600
    else:
        session.invalid_after = now + timedelta(hours=settings.JWT_REFRESH_EXPIRE)
        max_age = settings.JWT_REFRESH_EXPIRE * 3600
    db.add(session)
    db.commit()
    access_payload = {
        "role": "access",
        "session": session.id,
        "identity": identity,
        "type": "user",
        "exp": now + timedelta(minutes=settings.JWT_ACCESS_EXPIRE)
    }
    refresh_payload = {
        "role": "refresh",
        "session": session.id,
        "identity": identity,
        "type": f"user:{long}",
        "exp": session.invalid_after
    }
    access = encode_token(access_payload)
    refresh = encode_token(refresh_payload)
    set_cookie(access, response, max_age)
    return Refresh(refresh=refresh)


def verify_user_access(access: str, request: Request, db: Session) -> UserSession:
    access_payload = decode_token(access, "access")
    session: UserSession = db.query(UserSession).get(access_payload["session"])
    if session is None:
        raise errors.unauthorized()
    if session.fingerprint != get_user_agent_info(request) or session.identity != access_payload["identity"]:
        db.delete(session)
        db.commit()
        raise errors.unauthorized()
    return session


def refresh_user_tokens(access: str, refresh: str, request: Request, response: Response, db: Session) -> Refresh:
    access_payload = decode_token(access, "access", suppress=True)
    refresh_payload = decode_token(refresh, "refresh")
    if access_payload["identity"] != refresh_payload["identity"]:
        raise errors.token_validation_failed()
    session: UserSession = db.query(UserSession).get(access_payload["session"])
    if session is None:
        raise errors.unauthorized()
    if session.fingerprint != get_user_agent_info(request) or session.identity != access_payload["identity"]:
        db.delete(session)
        db.commit()
        raise errors.unauthorized()

    now = datetime.now(timezone.utc)
    identity = f"{uuid.uuid1(int(now.timestamp()))}"
    session.identity = identity
    long = refresh_payload["type"].endswith("True")
    if long:
        session.invalid_after = now + timedelta(hours=settings.JWT_REFRESH_LONG_EXPIRE)
        max_age = settings.JWT_REFRESH_LONG_EXPIRE * 3600
    else:
        session.invalid_after = now + timedelta(hours=settings.JWT_REFRESH_EXPIRE)
        max_age = settings.JWT_REFRESH_EXPIRE * 3600
    db.commit()
    access_payload = {
        "role": "access",
        "session": session.id,
        "identity": identity,
        "type": "user",
        "exp": now + timedelta(minutes=settings.JWT_ACCESS_EXPIRE)
    }
    refresh_payload = {
        "role": "refresh",
        "session": session.id,
        "identity": identity,
        "type": f"user:{long}",
        "exp": session.invalid_after
    }
    access = encode_token(access_payload)
    refresh = encode_token(refresh_payload)
    set_cookie(access, response, max_age)
    return Refresh(refresh=refresh)


async def get_user_session(request: Request, access: str = Cookie(None),
                           db: Session = Depends(get_database)) -> UserSession:
    """Получение сессии участника организации"""
    return verify_user_access(access, request, db)


async def get_user(session: UserSession = Depends(get_user_session)) -> User:
    """Получение участника организации"""
    return session.user


async def get_admin(session: UserSession = Depends(get_user_session), db: Session = Depends(get_database)):
    if db.query(Admin).filter_by(id=session.user.id).first() is not None:
        return session.user
    else:
        raise errors.access_denied()
