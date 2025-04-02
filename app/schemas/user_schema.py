from pydantic import BaseModel, EmailStr, Field, AfterValidator
from typing import Optional
from datetime import datetime
from ..helpers.helper import hash_password
from typing import Annotated


class BaseUser(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str = Field(min_length=6)
    email: EmailStr

def password_hash(value: str):
    return hash_password(value)

class CreateUser(BaseUser):
    password: Annotated[str, AfterValidator(password_hash)] = Field(min_length=5)


class ListUser(BaseUser):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


