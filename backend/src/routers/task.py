import datetime
import logging
import random
import traceback

import errors

from fastapi import APIRouter, Depends, Path
from sqlalchemy import text
from sqlalchemy.orm import load_only
from typing import Union

from auth import get_user
from models.audio import AudioFragment, Labeling, Validation
from models.user import UserStatistics, Project
from models import settings as permissions
from schemas.task import TranscribationCreate, FragmentTask, VerifyResult, TaskType, LabelingCreate, ClassifyingCreate
from db import get_database, Session
from db.session import engine
from settings import settings

import s3

router = APIRouter()


def task_transcribation(user, db, started_task=None, started_task_check=True) -> Union[Labeling, None]:
    # Проверка на наличие незаконченной транскрибации
    if started_task_check:
        transcribation = db.query(Labeling).join(AudioFragment, Labeling.audio_id == AudioFragment.id)
        transcribation = transcribation.filter(Labeling.user_id == user.id,
                                               Labeling.finished == False,
                                               AudioFragment.task_type == TaskType.transcribate.value).first()

    else:
        transcribation = started_task
    # Если у пользователя нет незаконченных транскрибаций, то выдаем новый фрагмент
    if transcribation is None:
        with engine.connect() as conn:
            task = f'(select a.* from audio_fragment as a left join labeling as t on a.id = t.audio_id where ' \
                   f'a.finished = FALSE and a.task_type = \'transcribate\' and ' \
                   f'a.id not in (select a.id from audio_fragment  as a inner join ' \
                   f'labeling as t on a.id = t.audio_id  where a.finished = FALSE and t.user_id = {user.id}) ' \
                   f'and a.project_id in (select project_users.project_id from project_users ' \
                   f'where project_users.user_id = {user.id}) ' \
                   f'group by a.id having count(t.id) < {settings.MAX_USERS_WITH_FRAGMENT} order by a.id);'
            fragment = conn.execute(text(task))
            fragment = fragment.first()

            db.commit()
        if fragment is None:
            return None
        transcribation = Labeling(
            audio_id=fragment.id,
            user_id=user.id,
            started_at=datetime.datetime.now()
        )
        db.add(transcribation)
        db.commit()
    else:
        transcribation.started_at = datetime.datetime.now()
        db.commit()

    return transcribation


def task_verify(user, db, started_task=None, started_task_check=True) -> Union[Validation, None]:
    """Проверка на наличие фрагмента, где пользователь уже начал валидацию транскрибации"""
    if started_task_check:
        started_validation = db.query(Validation).filter_by(validated_by=user.id, valid=None).first()
    else:
        started_validation = started_task
    # Создание новой задачи на валидацию транскрибации
    if started_validation is None:
        with engine.connect() as conn:
            task = f'(select t.* from labeling as t left join audio_fragment as a on t.audio_id = a.id where ' \
                   f't.finished = TRUE and a.task_type = \'transcribate\' and t.user_id != {user.id} and ' \
                   f't.id not in (select validation.labeling_id from validation) ' \
                   f'and a.project_id in (select project_users.project_id from project_users ' \
                   f'where project_users.user_id = {user.id}));'
            transcribation = conn.execute(text(task))
            transcribation = transcribation.first()

            db.commit()

        if transcribation is not None:
            validation = Validation(labeling_id=transcribation.id,
                                    validated_by=user.id)
            db.add(validation)
            db.commit()
        else:
            return None
    else:
        validation = started_validation

    return validation


def task_classify(user, db, started_task=None, started_task_check=True) -> Union[Labeling, None]:
    if started_task_check:
        started_classification = db.query(Labeling).join(AudioFragment, Labeling.audio_id == AudioFragment.id)
        started_classification = (started_classification.filter(Labeling.user_id == user.id,
                                                                Labeling.finished == False,
                                                                AudioFragment.task_type == TaskType.classify.value).
                                  first())
    else:
        started_classification = started_task
    if started_classification is None:
        with engine.connect() as conn:
            task = f'(select a.* from audio_fragment as a left join labeling as c on a.id = c.audio_id ' \
                   f'where a.finished = FALSE and a.task_type = \'classify\' and a.id not in ' \
                   f'(select a.id from audio_fragment as a inner join labeling as c on a.id = c.audio_id ' \
                   f'and c.user_id = {user.id}) and ' \
                   f'a.project_id in (select project_users.project_id from project_users ' \
                   f'where project_users.user_id = {user.id}) ' \
                   f'group by a.id having count(c.id) < {settings.MAX_USERS_WITH_FRAGMENT} order by a.id);'
            fragment = conn.execute(text(task))
            fragment = fragment.first()

            db.commit()

        if fragment is None:
            return None

        classification = Labeling(
            audio_id=fragment.id,
            user_id=user.id,
            started_at=datetime.datetime.now()
        )
        db.add(classification)
        db.commit()
    else:
        classification = started_classification

    return classification


def task_label(user, db, started_task=None, started_task_check=True) -> Union[Labeling, None]:
    if started_task_check:
        started_labeling = db.query(Labeling).join(AudioFragment, Labeling.audio_id == AudioFragment.id)
        started_labeling = started_labeling.filter(Labeling.user_id == user.id,
                                                   Labeling.finished == False,
                                                   AudioFragment.task_type == TaskType.label.value).first()
    else:
        started_labeling = started_task
    if started_labeling is None:
        with engine.connect() as conn:
            task = f'(select a.* from audio_fragment as a left join labeling as c on a.id = c.audio_id ' \
                   f'where a.finished = FALSE and a.task_type = \'label\' and a.id not in ' \
                   f'(select a.id from audio_fragment as a inner join labeling as c on a.id = c.audio_id ' \
                   f'and c.user_id = {user.id}) and ' \
                   f'a.project_id in (select project_users.project_id from project_users ' \
                   f'where project_users.user_id = {user.id})' \
                   f'group by a.id having count(c.id) < {settings.MAX_USERS_WITH_FRAGMENT} order by a.id);'
            fragment = conn.execute(text(task))
            fragment = fragment.first()

            db.commit()

        if fragment is None:
            return None
        labeling = Labeling(
            audio_id=fragment.id,
            user_id=user.id,
            started_at=datetime.datetime.now()
        )
        db.add(labeling)
        db.commit()
    else:
        labeling = started_labeling

    return labeling


@router.post("/transcribation/{task_id}", status_code=204,
             responses=errors.with_errors(errors.transcribation_not_found(),
                                          errors.task_is_not_available(),
                                          errors.permissions_not_found()))
async def create_transcribation(transribation: TranscribationCreate,
                                task_id: int = Path(title="Id of transcribation"),
                                user=Depends(get_user),
                                db: Session = Depends(get_database)):
    """Принимает транскрибацию и сохраняет ее"""
    task_permission = db.query(permissions.UserPermissions).filter_by(id=user.id).first()
    if task_permission is None:
        raise errors.permissions_not_found()
    elif task_permission.transcribate.value.endswith("block"):
        raise errors.task_is_not_available()

    new_transcribation = db.query(Labeling).filter_by(id=task_id, user_id=user.id).first()
    if not new_transcribation:
        raise errors.audio_not_found()
    if not new_transcribation.finished:
        new_transcribation.labeling = {"trb": transribation.trb}
        new_transcribation.finished = True
        new_transcribation.finished_at = datetime.datetime.now()

        # вложенная транзакция
        db.begin_nested()
        db.execute(text('LOCK TABLE user_statistics IN ROW EXCLUSIVE MODE;'))
        user_stat = db.query(UserStatistics).with_for_update().filter_by(
            user_id=new_transcribation.user_id).first()
        if user_stat:
            user_stat.transcribations_created += 1
            user_stat.total += 1
            db.commit()  # завершение транзакции
        else:
            db.rollback()
            raise errors.user_not_found()

        db.commit()

        fragment = db.query(AudioFragment).filter_by(id=new_transcribation.audio_id).first()
        transribations = (db.query(Labeling).join(Validation, Labeling.id == Validation.labeling_id).
                          filter(Labeling.audio_id == fragment.id).all())
        if (transribations is not None and
                db.query(Validation).filter(Validation.labeling_id.in_([trb.id for trb in transribations])).count() >=
                settings.MAX_USERS_WITH_FRAGMENT):
            fragment.finished = True
            db.commit()
        else:
            fragment.task_count += 1
            db.commit()


@router.post("/label/{task_id}", status_code=204)
async def create_labeling(task_id: int, params: LabelingCreate, user=Depends(get_user),
                          db: Session = Depends(get_database)):
    task_permission = db.query(permissions.UserPermissions).filter_by(id=user.id).first()
    if task_permission is None:
        raise errors.permissions_not_found()
    elif task_permission.label.value.endswith("block"):
        raise errors.task_is_not_available()
    new_labeling = db.query(Labeling).filter_by(id=task_id,
                                                user_id=user.id).first()
    if new_labeling is None:
        raise errors.audio_not_found()
    if not new_labeling.finished:
        new_labeling.labeling = {"labeling": params.label}
        new_labeling.finished = True
        new_labeling.finished_at = datetime.datetime.now()
        db.commit()

        # Обновление статистики
        user_statistics = (db.query(UserStatistics).options(load_only(UserStatistics.audio_labeled,
                                                                      UserStatistics.total)).
                           filter_by(user_id=user.id).first())

        user_statistics.audio_labeled += 1
        user_statistics.total += 1
        db.commit()

        #  Завершение задачи
        fragment = db.query(AudioFragment).filter_by(id=new_labeling.audio_id).first()
        if db.query(Labeling).filter_by(audio_id=fragment.id).count() >= \
                settings.MAX_USERS_WITH_FRAGMENT:
            fragment.finished = True
            db.commit()
        else:
            fragment.task_count += 1
            db.commit()


@router.post("/classify/{task_id}", status_code=204)
async def create_classification(task_id: int, params: ClassifyingCreate,
                                user=Depends(get_user),
                                db: Session = Depends(get_database)):
    task_permission = db.query(permissions.UserPermissions).filter_by(id=user.id).first()
    if task_permission is None:
        raise errors.permissions_not_found()
    elif task_permission.classify.value.endswith("block"):
        raise errors.task_is_not_available()
    new_classifying = db.query(Labeling).filter_by(id=task_id,
                                                   user_id=user.id).first()
    if new_classifying is None:
        raise errors.audio_not_found()
    if not new_classifying.finished:
        new_classifying.labeling = {"class": params.label}
        new_classifying.finished = True
        new_classifying.finished_at = datetime.datetime.now()

        # Обновление статистики
        user_statistics = (db.query(UserStatistics).options(load_only(UserStatistics.audio_classificated,
                                                                      UserStatistics.total)).
                           filter_by(user_id=user.id).first())

        user_statistics.audio_classificated += 1
        user_statistics.total += 1
        db.commit()
        # Завершение задачи
        fragment = db.query(AudioFragment).filter_by(id=new_classifying.audio_id).first()
        if db.query(Labeling).filter_by(audio_id=fragment.id).count() >= \
                settings.MAX_USERS_WITH_FRAGMENT:
            fragment.finished = True
            db.commit()
        else:
            fragment.task_count += 1
            db.commit()


@router.post("/verify/transcribation/{task_id}", status_code=204,
             responses=errors.with_errors(errors.transcribation_not_found(),
                                          errors.task_is_not_available(),
                                          errors.permissions_not_found()))
async def verify_transcribation(result: VerifyResult,
                                task_id: int,
                                user=Depends(get_user),
                                db: Session = Depends(get_database)):
    """Принятие задачи на верификацию фрагмента"""
    task_permission = db.query(permissions.UserPermissions).filter_by(id=user.id).first()
    if task_permission is None:
        raise errors.permissions_not_found()
    elif task_permission.validate.value.endswith("block"):
        raise errors.task_is_not_available()
    validation = db.query(Validation).filter_by(id=task_id).first()
    if validation is None:
        raise errors.audio_not_found()

    if validation.validated_by != user.id:
        raise errors.transcribation_unavailable()

    if validation.valid is None:
        validation.valid = result.valid
        validation.validated_at = datetime.datetime.now()

        # вложенная транзакция
        db.begin_nested()
        db.execute(text('LOCK TABLE user_statistics IN ROW EXCLUSIVE MODE;'))
        user_valid_stat = db.query(UserStatistics).with_for_update().filter_by(
            user_id=user.id).first()
        user_create_stat = db.query(UserStatistics).with_for_update().filter_by(
            user_id=validation.labeling.user_id).first()

        if user_valid_stat and user_create_stat:
            # добавить +1 validated для валидирующего
            user_valid_stat.validated += 1
            user_valid_stat.total += 1

            # добавить +1 в correct_transcribations/incorrect_transcribations для проверяемого
            if validation.valid:
                user_create_stat.correct_transcribations += 1
            else:
                user_create_stat.incorrect_transcribations += 1

            db.commit()  # завершение транзакции

        else:
            db.rollback()
            raise errors.user_not_found()

        db.commit()


@router.post("/random", response_model=FragmentTask,
             responses=errors.with_errors(errors.no_transcribations_available(),
                                          errors.no_audio_available(),
                                          errors.no_tasks_available()))
async def get_random_task(user=Depends(get_user), db: Session = Depends(get_database)):
    """Выдача случайной задачи"""
    # Создание списка доступных задач на основе прав
    task_select = []
    permission = db.query(permissions.UserPermissions).filter_by(id=user.id).first()
    if permission.transcribate.value.endswith("allow"):
        task_select.append(TaskType.transcribate.value)
    if permission.validate.value.endswith("allow"):
        task_select.append(TaskType.verify.value)
    if permission.label.value.endswith("allow"):
        task_select.append(TaskType.label.value)
    if permission.classify.value.endswith("allow"):
        task_select.append(TaskType.classify.value)
    random.shuffle(task_select)

    # Проверка наличия незаконченной разрешенной задачи
    if TaskType.transcribate.value in task_select:
        transcribation = db.query(Labeling).join(AudioFragment, Labeling.audio_id == AudioFragment.id)
        transcribation = transcribation.filter(Labeling.user_id == user.id,
                                               Labeling.finished == False,
                                               AudioFragment.task_type == TaskType.transcribate.value).first()
    else:
        transcribation = None
    if TaskType.verify.value in task_select:
        started_transcribation = db.query(Validation).filter_by(validated_by=user.id,
                                                                valid=None).first()
    else:
        started_transcribation = None
    if TaskType.label.value in task_select:
        started_labeling = db.query(Labeling).join(AudioFragment, Labeling.audio_id == AudioFragment.id)
        started_labeling = started_labeling.filter(Labeling.user_id == user.id,
                                                   Labeling.finished == False,
                                                   AudioFragment.task_type == TaskType.label.value).first()
    else:
        started_labeling = None
    if TaskType.classify.value in task_select:
        started_classification = db.query(Labeling).join(AudioFragment, Labeling.audio_id == AudioFragment.id)
        started_classification = (started_classification.filter(Labeling.user_id == user.id,
                                                                Labeling.finished == False,
                                                                AudioFragment.task_type == TaskType.classify.value).
                                  first())
    else:
        started_classification = None

    # Создание приоритета для незаконченной разрешенной задачи
    if (transcribation is None and started_transcribation and started_labeling is None and
            started_classification is None):
        task_select = [TaskType.verify.value]
    elif (started_transcribation is None and transcribation and started_labeling is None and
          started_classification is None):
        task_select = [TaskType.transcribate.value]
    elif (started_labeling and started_transcribation is None and transcribation is None and
          started_classification is None):
        task_select = [TaskType.label.value]
    elif (started_classification and started_labeling is None and transcribation is None and
          started_transcribation is None):
        task_select = [TaskType.classify.value]

    task = None
    for task_choice in task_select:
        if task_choice == TaskType.transcribate.value:
            """Возвращает случайный аудиофрагмент для транскрибации"""
            transcribation = task_transcribation(user, db, started_task=transcribation, started_task_check=False)
            if transcribation is None:
                continue

            # Запрос аудио фрагмента для разметки
            fragment = db.query(AudioFragment).filter_by(
                id=transcribation.audio_id).first()
            if fragment is None:
                continue
            original = "Problem with s3"
            try:
                s3_session = s3.S3()
                original = s3_session.get_url(fragment.s3_path)
            except Exception as e:
                logging.error(f"Got an exception while handling S3: {e}")
                logging.error(f"Traceback {traceback.format_exc()}")
            task = FragmentTask(s3_path=original,
                                additional_params={"trb": fragment.additional_params["orig_trb"]},
                                task_id=transcribation.id,
                                task_type='transcrib')
            break
        if task_choice == TaskType.verify.value:
            validation = task_verify(user, db, started_task=started_transcribation, started_task_check=False)
            if validation is None:
                continue

            # Запрос аудио фрагмента для разметки
            fragment = db.query(AudioFragment).filter_by(id=validation.labeling.audio_id).first()
            original = "Problem with s3"
            try:
                s3_session = s3.S3()
                original = s3_session.get_url(fragment.s3_path)
            except Exception as e:
                tb_str = traceback.format_exc()
                logging.error(f"Got an exception while handling S3: {e}")
                logging.error(f"Traceback {tb_str}")

            task = FragmentTask(s3_path=original,
                                additional_params={"trb": validation.labeling.labeling["trb"]},
                                task_id=validation.id,
                                task_type=TaskType.verify.value)
            break
        if task_choice == TaskType.classify.value:
            # Попытка создания задачи классификации
            classification = task_classify(user, db, started_task=started_classification, started_task_check=False)
            # Если нет доступной задачи классификации, то происходит попытка запросить другой тип задачи
            if classification is None:
                continue

            # Запрос аудио фрагмента для разметки
            fragment = db.query(AudioFragment).filter_by(id=classification.audio_id).first()
            original = "Problem with s3"
            try:
                s3_session = s3.S3()
                original = s3_session.get_url(fragment.s3_path)
            except Exception as e:
                tb_str = traceback.format_exc()
                logging.error(f"Got an exception while handling S3: {e}")
                logging.error(f"Traceback {tb_str}")

            # Запрос на доступные варианты в сегментации
            label_list = (db.query(Project).
                          options(load_only(Project.label_list)).
                          filter_by(id=fragment.project_id).
                          first())
            # Создание схемы задачи
            task = FragmentTask(s3_path=original,
                                additional_params={"label_list": label_list.label_list},
                                task_id=classification.id,
                                task_type=TaskType.classify.value)
            break
        if task_choice == TaskType.label.value:
            # Попытка создания задачи сегментации
            labeling = task_label(user, db, started_task=started_labeling, started_task_check=False)
            # Если нет доступной задачи сегментации, то происходит попытка запросить другой тип задачи
            if labeling is None:
                continue
            # Запрос аудио фрагмента для разметки
            fragment = db.query(AudioFragment).filter_by(id=labeling.audio_id).first()
            original = "Problem with s3"
            try:
                s3_session = s3.S3()
                original = s3_session.get_url(fragment.s3_path)
            except Exception as e:
                tb_str = traceback.format_exc()
                logging.error(f"Got an exception while handling S3: {e}")
                logging.error(f"Traceback {tb_str}")

            # Запрос на доступные варианты в сегментации
            label_list = (db.query(Project).
                          options(load_only(Project.label_list)).
                          filter_by(id=fragment.project_id).first())
            # Создание схемы задачи
            task = FragmentTask(s3_path=original,
                                additional_params={"label_list": label_list.label_list},
                                task_id=labeling.id,
                                task_type=TaskType.label.value)
            break
    if task is None:
        raise errors.no_tasks_available()
    else:
        return task
