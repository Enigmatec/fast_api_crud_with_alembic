from fastapi import APIRouter, Depends
from ..schemas.user_schema import ListUser
from ..models.user_model import User
from ..core.security import auth


class ProfileController:

    router = APIRouter(prefix="/profile", tags=["profile"])


    @router.get("", response_model=ListUser)
    async def profile(auth_user: User = Depends(auth)):
        return auth_user