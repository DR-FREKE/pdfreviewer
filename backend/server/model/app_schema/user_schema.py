from email.policy import default
from typing import List, Optional

from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    email: str 
    


class UserCreate(UserBase):
    password: str = Field(min_length=1)
    password_confirm: str = Field(min_length=1)

class UserUpdate(UserCreate):
    first_name: str
    last_name: str
    phone_number: str
    country: str
    gender: str
    DOB: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
