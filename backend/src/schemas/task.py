from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from enum import StrEnum


class TaskType(StrEnum):
    transcribate = "transcribate"
    verify = "verify"
    label = "label"
    classify = "classify"


class AudioFragmentGet(BaseModel):
    s3_path: str
    trb: str
    transcribation_id: int


class FragmentTask(BaseModel):
    s3_path: str
    additional_params: dict
    task_id: int
    task_type: str


class VerifyResult(BaseModel):
    valid: bool


class TranscribationGet(BaseModel):
    id: int
    user_id: int
    fragment_id: int
    started_at: datetime
    finished_at: datetime

    class Config:
        orm_mode = True


class TranscribationCreate(BaseModel):
    trb: str


class ClassifyingCreate(BaseModel):
    label: Optional[str]


class LabelingCreate(BaseModel):
    label: List[dict]


class StatisticsAll(BaseModel):
    fullname: str
    student: bool
    user_group: Optional[str]
    transcribations_created: int
    transcribations_validated: int
    transcribations_correct: float


class StatisticsRole(BaseModel):
    id: int
    fullname: str
    student: bool
    role: str
    user_group: Optional[str]
    transcribations_created: int
    transcribations_validated: int
    transcribations_correct: float
    audio_labeled: int
    audio_classified: int


class StatisticsAllFilter(BaseModel):
    limit: Optional[int]
    offset: Optional[int]
    student: Optional[bool]
    student_group: Optional[str]
