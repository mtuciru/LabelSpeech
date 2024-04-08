from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from settings import settings

engine = create_engine(
    "{}://{}:{}@{}:{}/{}".format(
        "postgresql",
        settings.DB_USERNAME,
        settings.DB_PASSWORD,
        settings.DB_ADDR,
        settings.DB_PORT,
        settings.DB_NAME,
    )
)

_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_database() -> Session:
    db: Session = _session()
    try:
        yield db
        db.flush()
        db.commit()

    except:
        db.rollback()
        raise
    finally:
        db.close()


@contextmanager
def with_database():
    db: Session = _session()
    try:
        yield db
        db.flush()
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
