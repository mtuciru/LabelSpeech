from sqlalchemy import ForeignKey, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base
from datetime import datetime


class AudioFragment(Base):
    __tablename__ = "audio_fragment"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    finished: Mapped[bool] = mapped_column(nullable=False, default=False)  # True когда сделано N транскрибаций
    s3_path: Mapped[str] = mapped_column(nullable=False)
    orig_trb: Mapped[str] = mapped_column(nullable=False)
    trb_count: Mapped[int] = mapped_column(nullable=False, default=0)


class Transcribation(Base):
    __tablename__ = "transcribations"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    fragment_id: Mapped[int] = mapped_column(ForeignKey("audio_fragment.id"), nullable=False)
    trb: Mapped[str] = mapped_column(nullable=True)
    finished: Mapped[bool] = mapped_column(nullable=False, default=False)
    started_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    finished_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    valid: Mapped[bool] = mapped_column(nullable=True)
    validated_by: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=True)
