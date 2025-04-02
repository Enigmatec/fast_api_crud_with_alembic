from app.database.session import get_session
from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.user_model import User
from passlib.context import CryptContext
from ..schemas.login_schema import LoginSchema


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_id(user_id: str, session: Session):
    user = session.get(User, user_id)
    return user

def get_user_by_email(email: str, session: Session):
    stmt = select(User).where(User.email == email)
    user = session.exec(statement=stmt).first()
    return user


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(plain_password):
    return pwd_context.hash(plain_password)


def authenticate(login: LoginSchema, session: Session):
    user = session.exec(select(User).where(User.email == login.email)).first()

    if not user or not verify_password(login.password, user.password):
        return None
    return user