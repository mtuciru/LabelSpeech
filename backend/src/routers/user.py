from sqlalchemy.sql import func
from fastapi import APIRouter, Depends

import errors

from db import get_database, Session
from models import user as usr
from models import settings as user_settings
from auth import get_user
from schemas.user import UserInfo, UpdateUserPermissions, AdminPermissionsRole

router = APIRouter()


@router.get("/me", response_model=UserInfo, responses=errors.with_errors(errors.user_not_found()))
async def get_account_info(user=Depends(get_user), db: Session = Depends(get_database)):
    """Получение информации пользователя о своих данных"""
    user_info = db.query(usr.User).filter_by(id=user.id).first()
    if not user_info:
        raise errors.user_not_found()

    statistics = db.query(usr.UserStatistics).filter_by(user_id=user.id).first()
    avg_total = db.query(func.avg(usr.UserStatistics.total)).scalar()
    avg_created = db.query(func.avg(usr.UserStatistics.created)).scalar()
    avg_validated = db.query(func.avg(usr.UserStatistics.validated)).scalar()
    return UserInfo(id=user_info.id,
                    role="admin" if db.query(usr.Admin).filter_by(id=user_info.id).first() else "user",
                    username=user_info.username,
                    fullname=user_info.fullname,
                    student=user_info.student,
                    group=user_info.student_group,
                    transcribations_created=statistics.created,
                    transcribations_validated=statistics.validated,
                    transcribations_correct=statistics.correct_transcribations / (statistics.correct_transcribations +
                                                                       statistics.incorrect_transcribations)
                    if statistics.correct_transcribations + statistics.incorrect_transcribations != 0 else 0,
                    deviation_total=(statistics.total/avg_total - 1)*100,
                    deviation_created=(statistics.created/avg_created - 1)*100,
                    deviation_validated=(statistics.validated/avg_validated - 1)*100)


@router.get("/me/permissions", response_model=AdminPermissionsRole)
async def get_user_permissions(user = Depends(get_user), db: Session = Depends(get_database)):
    """Получение прав пользователя"""
    user_info = db.query(usr.User).filter_by(id=user.id).first()
    user_permissions = db.query(user_settings.UserPermissions).filter_by(id=user.id).first()
    admin = db.query(usr.Admin).filter_by(id=user_info.id).first()
    if admin:
        return AdminPermissionsRole(id=user_info.id,
                                fullname=user_info.fullname,
                                role="admin",
                                group=user_info.student_group,
                                transcribation=user_permissions.transcribate.value,
                                validation=user_permissions.validate.value,
                                can_add_admins=admin.can_add_admins)
    else:
        return AdminPermissionsRole(id=user_info.id,
                                fullname=user_info.fullname,
                                role="user",
                                group=user_info.student_group,
                                transcribation=user_permissions.transcribate.value,
                                validation=user_permissions.validate.value,
                                can_add_admins=False)
    

@router.put("/me/permissions", status_code=204)
async def update_user_permissions(new_permissions: UpdateUserPermissions, user = Depends(get_user), 
                                  db: Session = Depends(get_database)):
    """Изменение прав пользователя"""
    permissions = db.query(user_settings.UserPermissions).filter_by(id=user.id).first()
    user_role = db.query(usr.Admin).filter_by(id=user.id).first()

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

    db.commit()
