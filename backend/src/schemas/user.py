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
    audio_labeled: int
    audio_classified: int
    transcribations_correct: float
    deviation_total: float
    deviation_created: float
    deviation_validated: float
    deviation_classify: float
    deviation_label: float

    class Config:
        orm_mode = True


class UserPermissions(BaseModel):
    user_role: str
    transcribation: str
    validation: str
    label: str
    classify: str


class AllUserPermissions(BaseModel):
    id: int
    fullname: str
    group: Optional[str]
    transcribation: str
    validation: str
    label: str
    classify: str


class UsersIdList(BaseModel):
    id_list: List[int]


class UserPermissionsRole(BaseModel):
    id: int
    fullname: str
    role: str
    group: Optional[str]
    transcribation: str
    validation: str
    label: str
    classify: str


class AdminPermissionsRole(BaseModel):
    id: int
    fullname: str
    role: str
    group: Optional[str]
    transcribation: str
    validation: str
    label: str
    classify: str
    can_add_admins: bool


class UpdateUsersPermissions(BaseModel):
    id_list: List[int]
    transcribation: Optional[Literal["admin_allow", "admin_block", "user_allow", "user_block"]]
    validation: Optional[Literal["admin_allow", "admin_block", "user_allow", "user_block"]]
    label: Optional[Literal["admin_allow", "admin_block", "user_allow", "user_block"]]
    classify: Optional[Literal["admin_allow", "admin_block", "user_allow", "user_block"]]


class UpdateUserPermissions(BaseModel):
    transcribation: Optional[Literal["user_allow", "user_block", "admin_allow", "admin_block"]]
    validation: Optional[Literal["user_allow", "user_block", "admin_allow", "admin_block"]]
    label: Optional[Literal["admin_allow", "admin_block", "user_allow", "user_block"]]
    classify: Optional[Literal["admin_allow", "admin_block", "user_allow", "user_block"]]


class UserPermissionStatistics(BaseModel):
    id: int
    fullname: str
    role: str
    group: Optional[str]
    transcribation: str
    validation: str
    classify: str
    label: str
    transcribations_created: int
    transcribations_validated: int
    transcribations_correct: float
    deviation_total: float
    deviation_created: float
    deviation_validated: float
    audio_labeled: int
    audio_classified: float
    deviation_classify: int
    deviation_label: float


class UserProjectGet(BaseModel):
    id: int
    name: str
