from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List, Any, Dict


class ProjectBaseInfo(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    owner: str


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str]
    label_list: List[Dict[Any, Any]]


class ProjectUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    label_list: Optional[list]


class ProjectInfo(BaseModel):
    id: int
    name: str
    description: Optional[str]
    label_list: list
    created_at: datetime
    owner: int

    class Config:
        orm_mode = True


class UsersInProject(BaseModel):
    user_id: List[int]
    project_id: List[int]
