import imp
from fastapi import FastAPI
from routes import user_route, auth_route

app = FastAPI();

app.include_router(user_route.router, tags=["users"]);
app.include_router(auth_route.router, tags=["auth"]);

