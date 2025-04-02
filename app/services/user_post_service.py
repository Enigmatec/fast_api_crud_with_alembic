from ..models.post_model import Post
from ..models.user_model import User
from sqlmodel import Session


async def list_posts(user: User, session: Session):
    return user.posts


async def create_post(user: User,  post: Post, session: Session):
    user.posts.append(post)
    session.commit()
    session.refresh(post)
    return post