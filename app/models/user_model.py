from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import  TYPE_CHECKING

if TYPE_CHECKING:
    from .post_model import Post
    

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str = Field(unique=True)
    password: str
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now, sa_column_kwargs={"onupdate": datetime.now})
    posts: list["Post"] = Relationship(back_populates="user")