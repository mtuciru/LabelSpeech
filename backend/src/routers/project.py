from sqlalchemy.exc import IntegrityError
import errors
from datetime import datetime
from sqlalchemy.orm import load_only
from typing import List
from fastapi import APIRouter, Depends, Body
from db import get_database, Session
from auth import get_admin
from models.user import Project, ProjectUsers, User
from schemas.project import ProjectBaseInfo, ProjectInfo, ProjectCreate, ProjectUpdate, UsersInProject

router = APIRouter()


@router.post("/", response_model=int, responses=errors.with_errors())
async def create_project(params: ProjectCreate = Body(), user=Depends(get_admin), db: Session = Depends(get_database)):
    """Создание проекта"""
    new_project = Project(name=params.name,
                          description=params.description,
                          label_list=params.label_list,
                          created_at=datetime.now(),
                          owner=user.id)
    db.add(new_project)
    db.commit()

    return new_project.id


@router.patch("/{project_id}", status_code=204, responses=errors.with_errors(errors.project_not_found()))
async def update_project(project_id: int, params: ProjectUpdate = Body(),
                         user=Depends(get_admin), db: Session = Depends(get_database)):
    """Обновление параметров проекта"""
    project = db.query(Project).options(load_only(Project.id)).filter_by(id=project_id).first()
    if project is None:
        raise errors.project_not_found()

    if params.name is not None:
        project.name = params.name
    if params.description is not None:
        project.description = params.description
    if params.label_list is not None:
        project.label_list = params.label_list

    db.commit()


@router.delete("/{project_id}", status_code=204, responses=errors.with_errors())
async def delete_project(project_id: int, user=Depends(get_admin), db: Session = Depends(get_database)):
    """Удаление проекта"""
    project = db.query(Project).options(load_only(Project.id)).filter_by(id=project_id).first()
    if project is None:
        raise errors.project_not_found()
    users_in_project = db.query(ProjectUsers).filter_by(project_id=project_id).all()
    if users_in_project is not None and len(users_in_project) > 0:
        for user in users_in_project:
            db.delete(user)
    db.delete(project)
    db.commit()


@router.get("/{project_id}", response_model=ProjectInfo, responses=errors.with_errors(errors.project_not_found()))
async def get_project(project_id: int, user=Depends(get_admin), db: Session = Depends(get_database)):
    """Получение подробной информации о проекте"""
    project = db.query(Project).filter_by(id=project_id).first()
    if project is None:
        raise errors.project_not_found()
    return ProjectInfo.from_orm(project)


@router.get("/all/", response_model=List[ProjectBaseInfo])
async def get_projects_list(user=Depends(get_admin), db: Session = Depends(get_database)):
    """Получение краткой информации о всех проектах"""
    projects = db.query(Project).options(load_only(Project.id,
                                                   Project.name,
                                                   Project.owner,
                                                   Project.description,
                                                   Project.created_at)).all()
    if projects is None:
        return []

    owners = set([project.owner for project in projects])
    owners_info = {owner.id: owner.fullname for owner in
                   db.query(User).options(load_only(User.id, User.fullname)).filter(User.id.in_(owners)).all()}
    return [ProjectBaseInfo(id=project.id,
                            name=project.name,
                            description=project.description,
                            created_at=project.created_at,
                            owner=owners_info[project.owner]) for project in projects]


@router.post("/users/", status_code=204,
             responses=errors.with_errors(errors.project_not_found(),
                                          errors.user_not_found(),
                                          errors.user_already_in_group()))
async def add_users_in_projects(params: UsersInProject, user=Depends(get_admin),
                                db: Session = Depends(get_database)):
    """Добавление пользователя в проект"""
    projects = db.query(Project).options(load_only(Project.id)).filter(Project.id.in_(params.project_id)).all()
    if projects is None or len(projects) == 0:
        raise errors.project_not_found()

    users = db.query(User).options(load_only(User.id)).filter(User.id.in_(params.user_id)).all()
    if users is None or len(users) == 0:
        raise errors.user_not_found()

    for project in params.project_id:
        for user in params.user_id:
            db.add(ProjectUsers(user_id=user, project_id=project))
    try:
        db.commit()
    except IntegrityError:
        raise errors.user_already_in_group()


@router.delete("/users/", status_code=204,
               responses=errors.with_errors(errors.project_not_found(),
                                            errors.user_not_found(),
                                            errors.user_in_group_not_found()))
async def remove_users_from_projects(params: UsersInProject, user=Depends(get_admin),
                                     db: Session = Depends(get_database)):
    """Удаление пользователя из проекта"""
    project = db.query(Project).options(load_only(Project.id)).filter(Project.id.in_(params.project_id)).all()
    if project is None or len(project) == 0:
        raise errors.project_not_found()

    user = db.query(User).options(load_only(User.id)).filter(User.id.in_(params.user_id)).all()
    if user is None or len(project) == 0:
        raise errors.user_not_found()

    user_in_project = db.query(ProjectUsers).filter(ProjectUsers.user_id.in_(params.user_id),
                                                    ProjectUsers.project_id.in_(params.project_id)).all()
    if user_in_project is None or len(user_in_project) == 0:
        raise errors.user_in_group_not_found()
    for user in user_in_project:
        db.delete(user)
    db.commit()


@router.get("/{project_id}/user/all", response_model=List[int],
            responses=errors.with_errors(errors.project_not_found()))
async def get_users_in_project(project_id: int, user=Depends(get_admin), db: Session = Depends(get_database)):
    """Получение всех пользователей в проекте"""
    project = db.query(Project).options(load_only(Project.id)).filter_by(id=project_id).first()
    if project is None:
        raise errors.project_not_found()

    users_in_project = db.query(ProjectUsers).filter_by(project_id=project_id).all()
    return [user.user_id for user in users_in_project] if users_in_project is not None else []
