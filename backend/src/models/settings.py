import enum
from sqlalchemy import ForeignKey, TIMESTAMP, Enum
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class PermissionLevel(enum.Enum):
    user_allow = "user_allow"
    user_block = "user_block"
    admin_allow = "admin_allow"
    admin_block = "admin_block"


class UserPermissions(Base):
    __tablename__ = "user_permissions"
    id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete='CASCADE'), primary_key=True, autoincrement=True)
    transcribate: Mapped[str] = mapped_column(Enum(PermissionLevel), nullable=False,
                                              default=PermissionLevel.admin_block)
    validate: Mapped[str] = mapped_column(Enum(PermissionLevel), nullable=False,
                                          default=PermissionLevel.admin_block)
