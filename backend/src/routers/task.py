import datetime
import logging
import random
import traceback

import errors

from fastapi import APIRouter, Depends, Path
from sqlalchemy import text

from auth import get_user
from models import audio
from models import user as usr
from models import settings as permissions
from schemas.task import AudioFragment, TranscribationCreate, FragmentTask, VerifyResult, TaskType
from db import get_database, Session
from db.session import engine
from settings import settings

import s3

router = APIRouter()


def task_transcribation(user, db, started_task=False, started_task_check=True):
    # Проверка на наличие незаконченной транскрибации
    if started_task_check:
        transcribation = db.query(audio.Transcribation).filter_by(user_id=user.id, finished=False).first()
    else:
        transcribation = started_task
    # Если у пользователя нет незаконченных транскрибаций, то выдаем новый фрагмент
    if transcribation is None:
        with engine.connect() as conn:
            task = f'(select a.* from audio_fragment as a left join transcribations as t on a.id = t.fragment_id where '\
                   f'a.finished = FALSE and a.id not in (select a.id from audio_fragment  as a inner join ' \
                   f'transcribations as t on a.id = t.fragment_id  where a.finished = FALSE and t.user_id = {user.id}) '\
                   f'group by a.id having count(t.id) < {settings.MAX_USERS_WITH_FRAGMENT} order by a.id);'
            fragment = conn.execute(text(task))
            fragment = fragment.first()

        db.commit()
        if fragment is None:
            return None
        transcribation = audio.Transcribation(user_id=user.id,
                                              fragment_id=fragment.id,
                                              trb=None,
                                              finished=False,
                                              started_at=datetime.datetime.now(),
                                              finished_at=None,
                                              valid=None)
        db.add(transcribation)
        db.commit()
    else:
        transcribation.started_at = datetime.datetime.now()
        db.commit()

    return transcribation


def task_verify(user, db, started_task=None, started_task_check=True):
    """Проверка на наличие фрагмента, где пользователь уже начал валидацию транскрибации"""
    if started_task_check:
        started_transcribation = db.query(audio.Transcribation).filter_by(validated_by=user.id, valid=None).first()
    else:
        started_transcribation = started_task
    if started_transcribation is None:
        transcribation = db.query(audio.Transcribation).filter(audio.Transcribation.valid == None,
                                                               audio.Transcribation.validated_by == None,
                                                               audio.Transcribation.finished == True,
                                                               audio.Transcribation.user_id != user.id).first()
        if transcribation is not None:
            transcribation.validated_by = user.id
            db.commit()
    else:
        transcribation = started_transcribation

    return transcribation


@router.get("/transcribate", response_model=AudioFragment, responses=errors.with_errors(errors.fragment_unavailable(),
                                                                                        errors.no_audio_available()))
async def get_fragment_for_transcibation(user=Depends(get_user), db: Session = Depends(get_database)):
    """Возвращает случайный аудиофрагмент для транскрибации"""
    # Проверка наличия прав на работу с выбранной задачей
    task_permission = db.query(permissions.UserPermissions).filter_by(id=user.id).first()
    if task_permission is None:
        raise errors.permissions_not_found()
    elif task_permission.transcribate.value.endswith("block"):
        raise errors.task_is_not_available()

    transcribation = task_transcribation(user, db)
    if transcribation is None:
        raise errors.no_audio_available()

    # Получение фрагмента для
    fragment = db.query(audio.AudioFragment).filter_by(id=transcribation.fragment_id).first()
    original = "Problem with s3"
    if fragment is None:
        raise errors.no_audio_available()
    try:
        s3_session = s3.S3()
        original = s3_session.get_url(fragment.s3_path)
    except Exception as e:
        logging.error(f"Got an exception while handling S3: {e}")
        logging.error(f"Traceback {traceback.format_exc()}")

    return AudioFragment(s3_path=original,
                         trb=fragment.orig_trb,
                         transcribation_id=transcribation.id)


@router.post("/transcribation/{transcribationid}", status_code=204,
             responses=errors.with_errors(errors.transcribation_not_found(),
                                          errors.task_is_not_available(),
                                          errors.permissions_not_found()))
async def create_transcribation(transribation: TranscribationCreate,
                                transcribationid: int = Path(title="Id of transcribation"),
                                user=Depends(get_user),
                                db: Session = Depends(get_database)):
    """Принимает транскрибацию и сохраняет ее"""
    task_permission = db.query(permissions.UserPermissions).filter_by(id=user.id).first()
    if task_permission is None:
        raise errors.permissions_not_found()
    elif task_permission.transcribate.value.endswith("block"):
        raise errors.task_is_not_available()
    new_transcribation = db.query(audio.Transcribation).filter_by(id=transcribationid).first()
    if not new_transcribation:
        raise errors.audio_not_found()
    if not new_transcribation.finished:
        new_transcribation.trb = transribation.trb
        new_transcribation.finished = True
        new_transcribation.finished_at = datetime.datetime.now()

        # вложенная транзакция
        db.begin_nested()
        db.execute(text('LOCK TABLE user_statistics IN ROW EXCLUSIVE MODE;'))
        user_stat = db.query(usr.UserStatistics).with_for_update().filter_by(
            user_id=new_transcribation.user_id).first()
        if user_stat:
            # добавить +1 created
            user_stat.created += 1
            user_stat.total += 1
            db.commit()  # завершение транзакции
        else:
            db.rollback()
            raise errors.user_not_found()

        db.commit()

        fragment = db.query(audio.AudioFragment).filter_by(id=new_transcribation.fragment_id).first()
        if db.query(audio.Transcribation).filter_by(fragment_id=fragment.id, valid=True).count() >= \
                settings.MAX_USERS_WITH_FRAGMENT:
            fragment.finished = True
            fragment.trb_count += 1
            db.commit()


@router.post("/verify/{transcribationid}", status_code=204,
             responses=errors.with_errors(errors.transcribation_not_found(),
                                          errors.task_is_not_available(),
                                          errors.permissions_not_found()))
async def verify_transcribation(result: VerifyResult,
                                transcribationid: int = Path(title="Id of transcribation"),
                                user=Depends(get_user),
                                db: Session = Depends(get_database)):
    """Принятие задачи на верификацию фрагмента"""
    task_permission = db.query(permissions.UserPermissions).filter_by(id=user.id).first()
    if task_permission is None:
        raise errors.permissions_not_found()
    elif task_permission.validate.value.endswith("block"):
        raise errors.task_is_not_available()
    verified_transcribation = db.query(audio.Transcribation).filter_by(id=transcribationid).first()
    if verified_transcribation is None:
        raise errors.audio_not_found()

    if not verified_transcribation.finished:
        raise errors.transcribation_unavailable()

    if verified_transcribation.validated_by != user.id:
        raise errors.transcribation_unavailable()

    if verified_transcribation.valid is None:
        verified_transcribation.valid = result.valid

        # вложенная транзакция
        db.begin_nested()
        db.execute(text('LOCK TABLE user_statistics IN ROW EXCLUSIVE MODE;'))
        user_valid_stat = db.query(usr.UserStatistics).with_for_update().filter_by(
            user_id=verified_transcribation.validated_by).first()
        user_create_stat = db.query(usr.UserStatistics).with_for_update().filter_by(
            user_id=verified_transcribation.user_id).first()
        
        if user_valid_stat and user_create_stat:
            # добавить +1 validated для валидирующего
            user_valid_stat.validated += 1
            user_valid_stat.total += 1
                
            # добавить +1 в correct_transcribations/incorrect_transcribations для проверяемого
            if verified_transcribation.valid:
                user_create_stat.correct_transcribations += 1
            else:
                user_create_stat.incorrect_transcribations += 1
        
            db.commit()  # завершение транзакции
            
        else:
            db.rollback()
            raise errors.user_not_found()

        db.commit()


@router.get("/verify", response_model=AudioFragment, responses=errors.with_errors(errors.no_transcribations_available()))
async def get_transcribation_for_verify(user=Depends(get_user), db: Session = Depends(get_database)):
    """Выдача задачи на валидацию транскрибации"""
    task_permission = db.query(permissions.UserPermissions).filter_by(id=user.id).first()
    if task_permission is None:
        raise errors.permissions_not_found()
    elif task_permission.validate.value.endswith("block"):
        raise errors.task_is_not_available()

    transcribation = task_verify(user, db)

    if transcribation is None:
        raise errors.no_transcribations_available()

    fragment = db.query(audio.AudioFragment).filter_by(id=transcribation.fragment_id).first()

    if fragment is None:
        errors.fragment_unavailable()

    original = "Problem with s3"
    try:
        s3_session = s3.S3()
        original = s3_session.get_url(fragment.s3_path)
    except Exception as e:
        tb_str = traceback.format_exc()
        logging.error(f"Got an exception while handling S3: {e}")
        logging.error(f"Traceback {tb_str}")
    task = AudioFragment(s3_path=original,
                         trb=transcribation.trb,
                         transcribation_id=transcribation.id)

    return task


@router.post("/random", response_model=FragmentTask, responses=errors.with_errors(errors.no_transcribations_available(),
                                                                                  errors.no_audio_available(),
                                                                                  errors.no_tasks_available()))
async def get_random_task(user=Depends(get_user), db: Session = Depends(get_database)):
    """Выдача случайной задачи"""
    task = None
    # Создание списка доступных задач на основе прав
    task_select = []
    permission = db.query(permissions.UserPermissions).filter_by(id=user.id).first()
    if permission.transcribate.value.endswith("allow"):
        task_select.append(TaskType.transcibate.value)
    if permission.validate.value.endswith("allow"):
        task_select.append(TaskType.verify.value)
    random.shuffle(task_select)

    # Проверка наличия незаконченной разрешенной задачи
    if TaskType.transcibate.value in task_select:
        transcribation = db.query(audio.Transcribation).filter_by(user_id=user.id, finished=False).first()
    else:
        transcribation = None
    if TaskType.verify.value in task_select:
        started_transcribation = db.query(audio.Transcribation).filter_by(validated_by=user.id, valid=None).first()
    else:
        started_transcribation = None

    # Создание приоритета для незаконченной разрешенной задачи
    if transcribation is None and started_transcribation:
        task_select = [TaskType.verify.value]
    elif started_transcribation is None and transcribation:
        task_select = [TaskType.transcibate.value]

    for task in task_select:
        if task == TaskType.transcibate.value:
            """Возвращает случайный аудиофрагмент для транскрибации"""
            transcribation = task_transcribation(user, db, started_task=transcribation, started_task_check=False)
            if transcribation is None:
                continue
            fragment = db.query(audio.AudioFragment).filter_by(id=transcribation.fragment_id).first()
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
                                trb=fragment.orig_trb,
                                transcribation_id=transcribation.id,
                                task_type='transcrib')
            break
        if task == TaskType.verify.value:
            transcribation = task_verify(user, db, started_task=started_transcribation, started_task_check=False)
            if transcribation is None:
                continue

            fragment = db.query(audio.AudioFragment).filter_by(id=transcribation.fragment_id).first()

            original = "Problem with s3"
            try:
                s3_session = s3.S3()
                original = s3_session.get_url(fragment.s3_path)
            except Exception as e:
                tb_str = traceback.format_exc()
                logging.error(f"Got an exception while handling S3: {e}")
                logging.error(f"Traceback {tb_str}")

            task = FragmentTask(s3_path=original,
                                trb=transcribation.trb,
                                transcribation_id=transcribation.id,
                                task_type='verify')
            break
    if task is None:
        raise errors.no_tasks_available()
    else:
        return task
