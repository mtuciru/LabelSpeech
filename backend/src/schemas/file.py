from pydantic import BaseModel
from typing import Optional
from schemas.task import TaskType


class AdditionalParams(BaseModel):
    orig_trb: Optional[str]


class FileUpload(BaseModel):
    token: str
    task_type: TaskType
