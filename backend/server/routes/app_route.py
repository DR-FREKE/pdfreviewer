import imp
from fastapi import FastAPI
from . import user_route

app: FastAPI = FastAPI();

app.include_router(user_route.router)
