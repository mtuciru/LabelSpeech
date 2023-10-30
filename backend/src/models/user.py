from passlib.context import CryptContext
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy import Integer, String, TIMESTAMP, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List

from models.base import Base

pwd_context = CryptContext(schemes=["sha256_crypt"])


class Admin(Base):
    __tablename__ = "admin"
    id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete='CASCADE'), primary_key=True)
    can_add_admins: Mapped[bool] = mapped_column(nullable=False, default=False)


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(32), nullable=False)
    __password: Mapped[str] = mapped_column("password", String, nullable=False)
    fullname: Mapped[str] = mapped_column(String(32), nullable=False)
    student: Mapped[bool] = mapped_column(nullable=False)
    student_group: Mapped[str] = mapped_column(nullable=True)
    sessions: Mapped[List["UserSession"]] = relationship(back_populates="user", uselist=True, passive_deletes=True)

    @hybrid_property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = pwd_context.hash(password)

    @hybrid_method
    def verify_password(self, password):
        return pwd_context.verify(password, self.__password)


class UserSession(Base):
    __tablename__ = "user_session"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete='CASCADE'), nullable=False, index=True)
    fingerprint: Mapped[str] = mapped_column(nullable=False)
    invalid_after: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    identity: Mapped[str] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship(back_populates="sessions", uselist=False, passive_deletes=True)


class UserStatistics(Base):
    __tablename__ = "user_statistics"
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete='CASCADE'), primary_key=True)
    created: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    correct_transcribations: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    incorrect_transcribations: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    validated: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    total: Mapped[int] = mapped_column(Integer, nullable=False, default=0)