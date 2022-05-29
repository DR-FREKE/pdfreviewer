from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    phone_number: str
    country: str
    gender: str
    DOB: str


class UserCreate(UserBase):
    password: str
    password_confirm: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
