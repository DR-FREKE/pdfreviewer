import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = os.environ.get("DATABASE_URL")  # should come from the env file outside the module

engine = create_engine(SQLALCHEMY_DB_URL, echo=True) ## echo is used to see whatever sql transaction or operation is carried out

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
