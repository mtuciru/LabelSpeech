from sqlalchemy.orm import load_only
from sqlalchemy.sql import func

import errors
from fastapi import APIRouter, Depends
from typing import List
from db import get_database, Session
from models.user import User, UserStatistics, Admin
from models import settings as user_settings
from auth import get_admin
from schemas.user import UpdateUsersPermissions, UsersIdList, UserPermissionStatistics
from schemas.task import StatisticsAllFilter, StatisticsRole

router = APIRouter()


@router.post("/create", status_code=204, responses=errors.with_errors(errors.user_not_found(),
                                                                      errors.access_denied()))
async def give_admin_status(users_id: UsersIdList, user=Depends(get_admin), db: Session = Depends(get_database)):
    """Выдать пользователям статус администратора"""
    if not db.query(Admin).filter_by(id=user.id).first().can_add_admins:
        raise errors.access_denied()

    for user_upd in db.query(User).filter(User.id.in_(users_id.id_list)).all():
        if db.query(User).filter_by(id=user_upd.id).first() is not None \
                and db.query(Admin).filter_by(id=user_upd.id).first() is None:
            db.add(Admin(id=user_upd.id))
            db.commit()
        else:
            raise errors.user_not_found()


@router.delete("/delete", status_code=204, responses=errors.with_errors(errors.user_not_found(),
                                                                        errors.access_denied()))
async def delete_admin_status(user_id: int, user=Depends(get_admin), db: Session = Depends(get_database)):
    """Забрать у пользователя права администратора"""
    if (db.query(Admin).filter_by(id=user.id).first().can_add_admins or
            db.query(Admin).filter_by(id=user.id).first().id == user_id):
        former_admin = db.query(Admin).filter_by(id=user_id).first()
        if former_admin is not None:
            db.delete(former_admin)
            db.commit()
        else:
            raise errors.user_not_found()
    else:
        raise errors.access_denied()


@router.post("/info", response_model=List[UserPermissionStatistics])
async def get_users_permissions(users: UsersIdList, user=Depends(get_admin),
                                db: Session = Depends(get_database)):
    """Получить список прав пользователей и их статистику"""
    result = []
    avg_total = db.query(func.avg(UserStatistics.total)).scalar()
    avg_created = db.query(func.avg(UserStatistics.transcribations_created)).scalar()
    avg_validated = db.query(func.avg(UserStatistics.validated)).scalar()
    avg_labeled = db.query(func.avg(UserStatistics.audio_labeled)).scalar()
    avg_classified = db.query(func.avg(UserStatistics.audio_classificated)).scalar()
    for user_permissions in (db.query(user_settings.UserPermissions).
            filter(user_settings.UserPermissions.id.in_(users.id_list)).all()):
        user_data = db.query(User).filter_by(id=user_permissions.id).first()
        user_stat = db.query(UserStatistics).filter_by(user_id=user_data.id).first()
        result.append(UserPermissionStatistics(id=user_permissions.id,
                                               fullname=user_data.fullname,
                                               role="admin" if db.query(Admin).filter_by(id=user_permissions.id).first()
                                               else "user",
                                               group=user_data.student_group,
                                               transcribation=user_permissions.transcribate.value,
                                               validation=user_permissions.validate.value,
                                               classify=user_permissions.classify.value,
                                               label=user_permissions.label.value,
                                               audio_labeled=user_stat.audio_labeled,
                                               audio_classified=user_stat.audio_classificated,
                                               deviation_classify=(user_stat.audio_classificated / avg_classified - 1) * 100
                                               if user_stat.audio_classificated != 0 else 0,
                                               deviation_label=(user_stat.audio_labeled / avg_labeled - 1) * 100
                                               if user_stat.audio_labeled != 0 else 0,
                                               transcribations_created=user_stat.transcribations_created,
                                               transcribations_validated=user_stat.validated,
                                               transcribations_correct=user_stat.correct_transcribations / (
                                                           user_stat.correct_transcribations + user_stat.incorrect_transcribations)
                                               if user_stat.correct_transcribations + user_stat.incorrect_transcribations != 0 else 0,
                                               deviation_total=(user_stat.total / avg_total - 1) * 100,
                                               deviation_created=(user_stat.transcribations_created / avg_created - 1) * 100,
                                               deviation_validated=(user_stat.validated / avg_validated - 1) * 100
                                               if avg_validated != 0 else 0))
    return result


@router.put("/permissions", status_code=204)
async def update_users_permissions(new_permissions: UpdateUsersPermissions, user=Depends(get_admin),
                                   db: Session = Depends(get_database)):
    """Изменить права пользователей"""
    if db.query(Admin).filter_by(id=user.id).first().can_add_admins:
        for user_id in new_permissions.id_list:
            user_permissions = db.query(user_settings.UserPermissions).filter_by(id=user_id).first()
            if new_permissions.transcribation is not None:
                user_permissions.transcribate = new_permissions.transcribation
            if new_permissions.validation is not None:
                user_permissions.validate = new_permissions.validation
            if new_permissions.label is not None:
                user_permissions.label = new_permissions.label
            if new_permissions.classify is not None:
                user_permissions.classify = new_permissions.classify
    else:
        for user_id in new_permissions.id_list:
            if db.query(Admin).filter_by(id=user_id).first() is None or user_id == user.id:
                user_permissions = db.query(user_settings.UserPermissions).filter_by(id=user_id).first()
                if new_permissions.transcribation is not None:
                    user_permissions.transcribate = new_permissions.transcribation
                if new_permissions.validation is not None:
                    user_permissions.validate = new_permissions.validation
                if new_permissions.label is not None:
                    user_permissions.label = new_permissions.label
                if new_permissions.classify is not None:
                    user_permissions.classify = new_permissions.classify
    db.commit()


@router.post("/statistics/all", response_model=List[StatisticsRole])
async def get_all_statistics(filters: StatisticsAllFilter, admin=Depends(get_admin),
                             db: Session = Depends(get_database)):
    """Выдача списка статистики разметки студентов"""

    """Если параметры фильтрации не указаны или указаны некорректно, то выдается вся статистика"""
    if filters.limit:
        if filters.offset is None:
            filter_offset = 0
        else:
            filter_offset = filters.offset

        if filters.student is not None and filters.student_group is None:
            users = db.query(User).filter_by(
                student=filters.student
            ).limit(filters.limit).offset(filter_offset).all()
        elif filters.student is None and filters.student_group is not None:
            users = db.query(User).filter_by(
                student=filters.student,
                student_group=filters.student_group
            ).limit(filters.limit).offset(filter_offset).all()
        else:
            users = db.query(User).limit(filters.limit).offset(filter_offset).all()
    else:
        if filters.student is not None and filters.student_group is None:
            users = db.query(User).filter_by(student=filters.student).all()
        elif filters.student is None and filters.student_group is not None:
            users = db.query(User).filter_by(
                student=filters.student,
                student_group=filters.student_group
            ).all()
        else:
            users = db.query(User).all()

    results = []
    for user_stat in users:
        statistics = db.query(UserStatistics).filter_by(user_id=user_stat.id).first()
        results.append(StatisticsRole(
            id=user_stat.id,
            fullname=user_stat.fullname,
            student=user_stat.student,
            role="admin" if db.query(Admin).filter_by(id=user_stat.id).first() else "user",
            user_group=user_stat.student_group,
            transcribations_created=statistics.transcribations_created,
            transcribations_validated=statistics.validated,
            audio_labeled=statistics.audio_labeled,
            audio_classified=statistics.audio_classificated,
            transcribations_correct=statistics.correct_transcribations /
                                    (statistics.correct_transcribations + statistics.incorrect_transcribations)
            if statistics.correct_transcribations + statistics.incorrect_transcribations != 0 else 0
        ))

    return results


@router.get("/group/{group_name}", response_model=List[int])
async def get_users_from_group(group_name: str, admin=Depends(get_admin), db: Session = Depends(get_database)):
    """Получение id всех пользователей из указанной группы """
    users = db.query(User).options(load_only(User.id)).filter_by(student_group=group_name).all()
    return [user.id for user in users] if users is not None else []


@router.get("/groups/all", response_model=List[str])
async def get_all_groups(admin=Depends(get_admin), db: Session = Depends(get_database)):
    """Получение всех групп в системе"""
    groups = (db.query(User).options(load_only(User.student_group)).distinct(User.student_group).
              filter_by(student=True).all())
    return [group.student_group for group in groups] if groups is not None else []
