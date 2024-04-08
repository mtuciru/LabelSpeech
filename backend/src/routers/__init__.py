from fastapi import APIRouter

from routers.admin import router as admin
from routers.auth import router as auth
from routers.task import router as task
from routers.user import router as user
from routers.file import router as upload
from routers.project import router as project


router = APIRouter(prefix="/api")
router.include_router(auth, prefix="/user", tags=["Auth"])
router.include_router(task, prefix="/task", tags=["Task"])
router.include_router(admin, prefix="/admin", tags=["Admin"])
router.include_router(user, prefix="/user", tags=["User"])
router.include_router(upload, prefix="/file", tags=["File"])
router.include_router(project, prefix="/project", tags=["Project"])
