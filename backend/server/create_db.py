from database.connection import Base, engine
from model.app_models.user_model import User

print("Creating database...")
Base.metadata.create_all(engine)