from fastapi import APIRouter, UploadFile, Depends

import errors
import s3
import logging

from settings import settings
from db import get_database, Session
from models.audio import AudioFragment
from schemas.file import FileUpload, AdditionalParams

router = APIRouter()


@router.post("/upload", status_code=204)
async def create_file(file: UploadFile, project_id: int, main_params: FileUpload = Depends(),
                      additional_params: AdditionalParams = Depends(),
                      db: Session = Depends(get_database)):
    """Метод для загрузки файла в хранилище файлов"""
    if main_params.token == settings.S3_TOKEN:
        try:
            db.add(AudioFragment(s3_path="fragments/" + file.filename,
                                 additional_params=dict(additional_params),
                                 project_id=project_id,
                                 task_type=main_params.task_type))
            s3_session = s3.S3()
            s3_session.upload_file(file.file.read(), "fragments/" + file.filename)
        except Exception as e:
            logging.error(f"S3 is not available now!\n{e}")
            raise errors.unable_to_upload_file()
        else:
            db.commit()

    else:
        raise errors.access_denied()
