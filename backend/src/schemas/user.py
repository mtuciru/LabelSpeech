from typing import Optional, List, Literal
from pydantic import BaseModel


class UserInfo(BaseModel):
    id: int
    role: str
    username: str
    fullname: str
    student: bool
    group: Optional[str]
    transcribations_created: int
    transcribations_validated: int
    transcribations_correct: float
    deviation_total: float
    deviation_created: float
    deviation_validated: float

    class Config:
        orm_mode = True


class UserPermissions(BaseModel):
    user_role: str
    transcribation: str
    validation: str


class AllUserPermissions(BaseModel):
    id: int
    fullname: str
    group: Optional[str]
    transcribation: str
    validation: str


class UsersIdList(BaseModel):
    id_list: List[int]


class UserPermissionsRole(BaseModel):
    id: int
    fullname: str
    role: str
    group: Optional[str]
    transcribation: str
    validation: str


class AdminPermissionsRole(BaseModel):
    id: int
    fullname: str
    role: str
    group: Optional[str]
    transcribation: str
    validation: str
    can_add_admins: bool


class UpdateUsersPermissions(BaseModel):
    id_list: List[int]
    transcribation: Optional[Literal["admin_allow", "admin_block", "user_allow", "user_block"]]
    validation: Optional[Literal["admin_allow", "admin_block", "user_allow", "user_block"]]


class UpdateUserPermissions(BaseModel):
    transcribation: Optional[Literal["user_allow", "user_block", "admin_allow", "admin_block"]]
    validation: Optional[Literal["user_allow", "user_block", "admin_allow", "admin_block"]]


class UserPermissionStatistics(BaseModel):
    id: int
    fullname: str
    role: str
    group: Optional[str]
    transcribation: str
    validation: str
    transcribations_created: int
    transcribations_validated: int
    transcribations_correct: float
    deviation_total: float
    deviation_created: float
    deviation_validated: float
