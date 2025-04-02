from ..models.user_model import User
from sqlmodel import Session, select

async def create_user(user: User, session: Session):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


async def list_users(session: Session):
    return session.exec(select(User)).all()

