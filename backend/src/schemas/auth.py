from typing import Optional

from pydantic import BaseModel


class UserCredentials(BaseModel):
    login: str
    password: str
    remember_me: Optional[bool] = False


class Refresh(BaseModel):
    refresh: str


class SignUp(BaseModel):
    username: str
    password: str
    fullname: str
    student: bool
    student_group: str
