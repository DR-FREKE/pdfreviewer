import email
from sys import prefix
from fastapi import FastAPI, Depends
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from model.app_models import user_model
from database.connection import engine
from dependencies import get_header_token, get_query_token
from routes import user_route, auth_route, file_route

app = FastAPI()
# app = FastAPI(dependencies=[Depends(get_query_token)]) ## use when you've setup token

# @app.on_event("startup")
# def on_startup():
#     UserModel = user_model.User
#     user: list = [UserModel(email="solomonndi96@gmail.com", first_name="Ndifereke", last_name="Solomon", phone="08034717824")]
    

"""handle cors error that might come up when a request is sent"""
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_route.router, prefix="/api/v1", tags=["users"])
app.include_router(auth_route.router, prefix="/api/v1", tags=["auth"])
app.include_router(file_route.router, prefix="/api/v1", tags=["file"])


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run(app)
