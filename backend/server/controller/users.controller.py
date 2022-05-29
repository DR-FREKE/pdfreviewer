from sqlalchemy.orm import Session;
from model.app_models import user_model as models
from model.app_schema import user_schema

def get_users(db: Session, skip: int = 0, limit: int = 30):
    return db.query(models.User).offset(skip).limit(limit).all()