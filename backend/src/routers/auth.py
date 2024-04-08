from fastapi import APIRouter, Depends, Request, Response, Body, Cookie

import errors
from auth import init_user_tokens, get_user_session, refresh_user_tokens
from models.user import User, UserStatistics
from models.settings import UserPermissions, PermissionLevel

from db import get_database, Session
from schemas.auth import UserCredentials, Refresh, SignUp

router = APIRouter()


@router.post("/login", response_model=Refresh,
             responses=errors.with_errors(errors.invalid_credentials(), errors.token_validation_failed(),
                                          errors.token_expired()))
async def login_user(
        request: Request,
        response: Response,
        credentials: UserCredentials,
        db: Session = Depends(get_database)
):
    user = db.query(User).filter_by(username=credentials.login).first()
    if user is None:
        raise errors.invalid_credentials()
    if not user.verify_password(credentials.password):
        raise errors.invalid_credentials()
    return init_user_tokens(user, credentials.remember_me, request, response, db)


@router.delete("/logout", status_code=204,
               responses=errors.with_errors(errors.unauthorized(), errors.token_expired(),
                                            errors.token_validation_failed()))
async def logout_user(response: Response, user_session=Depends(get_user_session),
                      db: Session = Depends(get_database)):
    response.delete_cookie(key="access")
    db.delete(user_session)
    db.commit()


@router.post("/refresh", response_model=Refresh,
             responses=errors.with_errors(errors.unauthorized(), errors.token_expired(),
                                          errors.token_validation_failed()))
async def refresh(
        request: Request,
        response: Response,
        access: str = Cookie(None),
        params: Refresh = Body(),
        db: Session = Depends(get_database)
):
    return refresh_user_tokens(access, params.refresh, request, response, db)


@router.post("/signup", status_code=204)
async def signup_user(user: SignUp, db: Session = Depends(get_database)):
    if len(user.username) < 3:
        raise errors.user_create_error("Username is too short (must be >3 symbols)!")

    if len(user.password) < 8:
        raise errors.user_create_error("Password is too short (must be >8 symbols)!")

    if user.student and not user.student_group:
        raise errors.user_create_error("Student group is mandatory if student == true!")

    if db.query(User).filter_by(username=user.username).first():
        raise errors.user_create_error("User with such username already exits!")

    new_user = User(
            username=user.username,
            password=user.password,
            fullname=user.fullname,
            student=user.student,
            student_group=user.student_group if user.student else None
        )
    db.add(new_user)
    db.commit()

    db.add(UserPermissions(
        id=new_user.id,
        transcribate=PermissionLevel.admin_allow,
        validate=PermissionLevel.admin_allow,
        label=PermissionLevel.admin_allow,
        classify=PermissionLevel.admin_allow
    ))
    db.add(UserStatistics(
        user_id=new_user.id
    ))
    db.commit()
