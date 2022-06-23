import email
from fastapi import HTTPException, status
from sqlalchemy.orm import Session;

from dataclasses import dataclass
from model.app_models import user_model as models
from model.app_schema.user_schema import UserCreate

@dataclass
class RegisterController:

    @classmethod
    async def save(cls, db, user_instance):
        try:
            db.add(user_instance);
            db.commit();
            db.refresh(user_instance)
        except:
            db.rollback();
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    async def addUser(cls, db: Session, user: UserCreate):
        hashed_password = user.password+"shouldbehashed";
        new_user = models.User(email=user.email, hashed_password=hashed_password);
        
        await cls.save(db, new_user);
        return new_user