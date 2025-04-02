from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .user_model import User


class Post(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    content: str
    user_id : Optional[int] = Field(default=None, foreign_key="user.id")
    is_active: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now, sa_column_kwargs={"onupdate": datetime.now})
    user: Optional["User"] = Relationship(back_populates="posts")