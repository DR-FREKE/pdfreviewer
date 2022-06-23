from database.connection import Base, engine
from model.app_models.user_model import User
from model.app_models.file_model import File

print("Creating database...")
Base.metadata.create_all(engine)