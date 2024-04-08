from sqlalchemy import text

from settings import settings
from db.session import engine, with_database

import models


def create_admin():
    with with_database() as db:
        if db.query(models.user.Admin).count():
            return

        db.add(models.user.User(
            id=1,
            username=settings.ADMIN_EMAIL,
            fullname="Admin",
            student=False,
            password=settings.ADMIN_PASSWORD
        ))

        db.commit()
        db.add(models.settings.UserPermissions(
            id=1,
            transcribate=models.settings.PermissionLevel.admin_allow,
            validate=models.settings.PermissionLevel.admin_allow,
            label=models.settings.PermissionLevel.admin_allow,
            classify=models.settings.PermissionLevel.admin_allow
        ))
        db.add(models.user.Admin(
            id=1,
            can_add_admins=True
        ))
        db.add(models.user.UserStatistics(user_id=1))
        with engine.connect() as conn:
            conn.execute(text("SELECT setval('user_id_seq',1,true)"))

        db.commit()


def initdb():
    with with_database() as db:
        try:
            db.execute(text("CREATE EXTENSION hstore;"))
        except:
            pass
    models.base.Base.metadata.create_all(engine)
    try:
        create_admin()
    except Exception as exsp:
        print(exsp)
        print(type(exsp))
