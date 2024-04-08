from sqlalchemy import ForeignKey, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base
from datetime import datetime
from typing import Dict, Any
from sqlalchemy.dialects.postgresql import JSONB


class AudioFragment(Base):
    __tablename__ = "audio_fragment"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id"), nullable=False)
    finished: Mapped[bool] = mapped_column(nullable=False, default=False)
    s3_path: Mapped[str] = mapped_column(nullable=False)
    additional_params: Mapped[Dict[str, Any]] = mapped_column(JSONB, nullable=False)
    task_type: Mapped[str] = mapped_column(nullable=False)
    task_count: Mapped[int] = mapped_column(nullable=False, default=0)


class Labeling(Base):
    __tablename__ = "labeling"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    audio_id: Mapped[int] = mapped_column(ForeignKey("audio_fragment.id"), nullable=False)
    labeling: Mapped[Dict[Any, Any]] = mapped_column(JSONB, nullable=True)
    finished: Mapped[bool] = mapped_column(nullable=False, default=False)
    started_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    finished_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)


class Validation(Base):
    __tablename__ = "validation"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    labeling_id: Mapped[int] = mapped_column(ForeignKey("labeling.id"), nullable=False)
    valid: Mapped[bool] = mapped_column(nullable=True)
    validated_by: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=True)
    validated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)

    labeling: Mapped["Labeling"] = relationship("Labeling", backref="validation")
