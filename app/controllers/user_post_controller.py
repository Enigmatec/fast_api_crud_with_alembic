from fastapi import APIRouter, Depends
from ..models.post_model import Post
from ..schemas.post_schema import PostSchema
from ..models.user_model import User
from ..core.security import auth
from sqlmodel import Session
from ..database.session import get_session
from ..services import user_post_service
from ..models.post_model import Post

class UserPostController:

    router = APIRouter(prefix="/posts", tags=["user posts"])

    @router.get("", response_model=list[Post])
    async def list_posts(user: User = Depends(auth),session: Session = Depends(get_session)):

        posts = await user_post_service.list_posts(user, session)
        return posts
    
    @router.post("", response_model=Post)
    async def create_post(postSchema: PostSchema, user: User = Depends(auth),session: Session = Depends(get_session)):

        post = Post(title=postSchema.title, content = postSchema.content)
        post = await user_post_service.create_post(user, post, session)
        return post

        

