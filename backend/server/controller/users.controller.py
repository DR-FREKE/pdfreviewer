from dataclasses import dataclass
from sqlalchemy.orm import Session;
from model.app_models import user_model as models
from model.app_schema import user_schema

@dataclass
class UserController:

    @classmethod
    async def get_users(self, db: Session, skip: int = 0, limit: int = 30):
        return db.query(models.User).offset(skip).limit(limit).all()