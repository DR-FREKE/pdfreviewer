from datetime import datetime
from email.policy import default
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
    first_name = Column(String, default=None)
    last_name = Column(String, default=None)
    phone_number = Column(String)
    country = Column(String, default=None)
    gender = Column(String, default=None)
    DOB = Column(String, default=None)
    created_at = Column(DateTime, default=datetime.utcnow)

