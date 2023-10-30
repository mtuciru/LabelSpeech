from fastapi import APIRouter, UploadFile, Depends

import errors
import s3
import logging

from settings import settings
from db import get_database, Session
from models import audio

router = APIRouter()


@router.post("/upload", status_code=204)
async def create_file(token: str, file: UploadFile, orig_trb: str, db: Session = Depends(get_database)):
    """Метод для загрузки файла в хранилище файлов"""
    if token == settings.S3_TOKEN:
        try:
            db.add(audio.AudioFragment(s3_path="/fragments" + file.filename,
                                       orig_trb=orig_trb))
            db.commit()
            s3_session = s3.S3()
            s3_session.upload_file(file.file.read(), file.filename)
        except Exception as e:
            logging.error(f"S3 is not available now!\n{e}")
            raise errors.unable_to_upload_file()
    else:
        raise errors.access_denied()
