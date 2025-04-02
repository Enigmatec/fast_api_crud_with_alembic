from pydantic import BaseModel, Field
from typing import Optional



class PostSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str = Field(min_length=5)
    content: str = Field(min_length=10)