from fastapi import HTTPException, status;
from sqlalchemy.orm import Session;

from dataclasses import dataclass;
from model.app_models import user_model as models;
from model.app_schema.user_schema import UserCreate;
from mail.mailer import Mailer;

@dataclass
class RegisterController:

    @classmethod
    async def save(cls, db: Session, user_instance: dict):
        try:
            db.add(user_instance);
            db.commit();
            db.refresh(user_instance);
        except:
            db.rollback();
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR);

    @classmethod
    async def getUserByEmail(cls, db: Session, email:str) -> dict:
        user = db.query(models.User).filter(models.User.email == email).one_or_none();
        return user;

    @classmethod
    async def addUser(cls, db: Session, user: UserCreate) -> dict:
        await Mailer.sendMail("solomonndi96@gmail.com")
        # if user.password != user.password_confirm:
        #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="passwords do not match!");
            
        # db_user = await cls.getUserByEmail(db, email=user.email);

        # if db_user:
        #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exist");
        
        # hashed_password = user.password+"shouldbehashed";
        # new_user = models.User(email=user.email, hashed_password=hashed_password);
        
        # await cls.save(db, new_user);
        # if new_user:
        #     ## call the send mail method
        #     await Mailer.sendMail(new_user.email)
        #     return new_user;