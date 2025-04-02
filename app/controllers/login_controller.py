from fastapi import APIRouter,Body, HTTPException, Depends
from ..schemas.login_schema import LoginSchema
from ..helpers.helper import authenticate
from sqlmodel import Session
from ..database.session import get_session
from ..core.security import create_token

class LoginController:
    router = APIRouter(prefix="/auth", tags=["Auth"])




    @router.post("/login")
    async def login(login: LoginSchema = Body(...), session: Session = Depends(get_session)):
        user = authenticate(login, session)
        if user is None:
            raise HTTPException(401, detail="Incorrect login credentials")
        token = create_token(user.id)
        return token

