import jwt
from decouple import config
from fastapi.security import OAuth2PasswordBearer
import time
from fastapi import Depends, HTTPException
from app.helpers.helper import get_user_by_id
from sqlmodel import Session
from ..database.session import get_session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")
JWT_EXPIRY = time.time() + int(config("JWT_EXPIRY"))



def create_token(user_id: str):
    payload = {"user_id" : user_id, "exp": JWT_EXPIRY}

    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token

def auth(token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        user_id = decode_token['user_id']
        if user_id is None:
            raise HTTPException(status_code=401, detail="unauthenticated")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="unauthenticated")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="unauthenticated")
    return get_user_by_id(user_id, session)