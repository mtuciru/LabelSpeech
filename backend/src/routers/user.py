from sqlalchemy.orm import load_only
from sqlalchemy.sql import func
from fastapi import APIRouter, Depends
from typing import List

import errors

from db import get_database, Session
from models.user import User, UserStatistics, Admin, ProjectUsers, Project
from models import settings as user_settings
from auth import get_user
from schemas.user import UserInfo, UpdateUserPermissions, AdminPermissionsRole, UserProjectGet

router = APIRouter()


@router.get("/me", response_model=UserInfo, responses=errors.with_errors(errors.user_not_found()))
async def get_account_info(user=Depends(get_user), db: Session = Depends(get_database)):
    """Получение информации пользователя о своих данных"""
    user_info = db.query(User).filter_by(id=user.id).first()
    if not user_info:
        raise errors.user_not_found()

    statistics = db.query(UserStatistics).filter_by(user_id=user.id).first()
    avg_total = db.query(func.avg(UserStatistics.total)).scalar()
    avg_created = db.query(func.avg(UserStatistics.transcribations_created)).scalar()
    avg_validated = db.query(func.avg(UserStatistics.validated)).scalar()
    avg_labeled = db.query(func.avg(UserStatistics.audio_labeled)).scalar()
    avg_classify = db.query(func.avg(UserStatistics.audio_classificated)).scalar()
    return UserInfo(id=user_info.id,
                    role="admin" if db.query(Admin).filter_by(id=user_info.id).first() else "user",
                    username=user_info.username,
                    fullname=user_info.fullname,
                    student=user_info.student,
                    group=user_info.student_group,
                    transcribations_created=statistics.transcribations_created,
                    transcribations_validated=statistics.validated,
                    audio_labeled=statistics.audio_labeled,
                    audio_classified=statistics.audio_classificated,
                    transcribations_correct=statistics.correct_transcribations / (statistics.correct_transcribations +
                                                                                  statistics.incorrect_transcribations)
                    if statistics.correct_transcribations + statistics.incorrect_transcribations != 0 else 0,
                    deviation_total=(statistics.total / avg_total - 1) * 100
                    if statistics.transcribations_created != 0 else 0,
                    deviation_created=(statistics.transcribations_created / avg_created - 1) * 100
                    if statistics.transcribations_created != 0 else 0,
                    deviation_validated=(statistics.validated / avg_validated - 1) * 100
                    if statistics.validated != 0 else 0,
                    deviation_classify=(statistics.audio_classificated / avg_classify - 1) * 100
                    if statistics.audio_classificated != 0 else 0,
                    deviation_label=(statistics.audio_labeled / avg_labeled - 1) * 100
                    if statistics.audio_labeled != 0 else 0)


@router.get("/me/permissions", response_model=AdminPermissionsRole)
async def get_user_permissions(user=Depends(get_user), db: Session = Depends(get_database)):
    """Получение прав пользователя"""
    user_info = db.query(User).filter_by(id=user.id).first()
    user_permissions = db.query(user_settings.UserPermissions).filter_by(id=user.id).first()
    admin = db.query(Admin).filter_by(id=user_info.id).first()
    if admin:
        return AdminPermissionsRole(id=user_info.id,
                                    fullname=user_info.fullname,
                                    role="admin",
                                    group=user_info.student_group,
                                    transcribation=user_permissions.transcribate.value,
                                    validation=user_permissions.validate.value,
                                    label=user_permissions.label.value,
                                    classify=user_permissions.classify.value,
                                    can_add_admins=admin.can_add_admins)
    else:
        return AdminPermissionsRole(id=user_info.id,
                                    fullname=user_info.fullname,
                                    role="user",
                                    group=user_info.student_group,
                                    transcribation=user_permissions.transcribate.value,
                                    validation=user_permissions.validate.value,
                                    label=user_permissions.label.value,
                                    classify=user_permissions.classify.value,
                                    can_add_admins=False)


@router.put("/me/permissions", status_code=204)
async def update_user_permissions(new_permissions: UpdateUserPermissions, user=Depends(get_user),
                                  db: Session = Depends(get_database)):
    """Изменение прав пользователя"""
    permissions = db.query(user_settings.UserPermissions).filter_by(id=user.id).first()
    user_role = db.query(Admin).filter_by(id=user.id).first()

    if new_permissions.transcribation is not None:
        # Если права строго заданы администратором, то право на их изменение есть только у администратора
        if permissions.transcribate.value.startswith("admin") and user_role is not None:
            permissions.transcribate = new_permissions.transcribation
        # Если права доступны для редактирования пользователем, то пользователь может изменить их только не строго
        # Администратор имеет полные права на их редактирование
        elif permissions.transcribate.value.startswith("user") and \
                ((user_role is None and new_permissions.transcribation.startswith("user")) or user_role is not None):
            permissions.transcribate = new_permissions.transcribation
    if new_permissions.validation is not None:
        if permissions.validate.value.startswith("admin") and user_role is not None:
            permissions.validate = new_permissions.validation
        elif permissions.validate.value.startswith("user") and \
                ((user_role is None and new_permissions.validation.startswith("user")) or user_role is not None):
            permissions.validate = new_permissions.validation
    if new_permissions.label is not None:
        if permissions.label.value.startswith("admin") and user_role is not None:
            permissions.label = new_permissions.label
        elif permissions.label.value.startswith("user") and \
                ((user_role is None and new_permissions.label.startswith("user")) or user_role is not None):
            permissions.label = new_permissions.label
    if new_permissions.classify is not None:
        if permissions.classify.value.startswith("admin") and user_role is not None:
            permissions.classify = new_permissions.classify
        elif permissions.classify.value.startswith("user") and \
                ((user_role is None and new_permissions.classify.startswith("user")) or user_role is not None):
            permissions.classify = new_permissions.classify

    db.commit()


@router.get("/me/projects", response_model=List[UserProjectGet])
async def get_users_projects(user=Depends(get_user), db: Session = Depends(get_database)):
    users_projects = db.query(ProjectUsers).filter_by(user_id=user.id).all()
    projects = [project.project_id for project in users_projects] if users_projects is not None else []
    project_info = db.query(Project).options(load_only(Project.name, Project.id)).filter(Project.id.in_(projects)).all()
    return [UserProjectGet(id=project.id, name=project.name) for project in project_info] if len(project_info) else []
