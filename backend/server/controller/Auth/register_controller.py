from fastapi import HTTPException, status
from sqlalchemy.orm import Session;

from dataclasses import dataclass
from model.app_models import user_model as models
from model.app_schema.user_schema import UserCreate

@dataclass
class RegisterController:

    @classmethod
    async def save(cls, user_instance):
        pass

    @classmethod
    async def addUser(cls, db: Session, user: UserCreate):
        return {"message":user.password}
        # return db.query(models.User).offset(skip).limit(limit).all()