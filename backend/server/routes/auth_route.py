from atexit import register
import imp
from unittest import result
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session;

from dependencies import get_header_token, get_db
from controller.Auth.register_controller import RegisterController as reg
from model.app_schema.user_schema import UserCreate, User


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    # dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}}
)

@router.post("/sign-up/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    register = await reg.addUser(db=db, user=user)
    return register
    
