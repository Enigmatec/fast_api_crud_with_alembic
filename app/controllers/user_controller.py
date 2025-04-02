from fastapi import APIRouter, Depends, HTTPException
from ..schemas.user_schema import CreateUser, ListUser
from ..services import user_service
from ..helpers.helper import hash_password
from ..database.session import get_session
from sqlmodel import Session
from ..models.user_model import User
from ..helpers.helper import get_user_by_email


class UserController:

    router = APIRouter(prefix="/users", tags=["user"])

    @router.get("/", response_model=list[ListUser])
    async def list_users(session: Session = Depends(get_session)):
        return await user_service.list_users(session)

    @router.post("/", response_model=User, response_model_exclude=["password"])
    async def create_user(user: CreateUser, session: Session = Depends(get_session)):

        if(get_user_by_email(user.email, session)):
            raise HTTPException(419, detail="email has been taken")

        user = User(name=user.name, email=user.email, password=user.password)
        user = await user_service.create_user(user, session=session)
        return user

    
