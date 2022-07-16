from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session;

from dependencies import get_header_token, get_db
from controller.Auth.register_controller import RegisterController as reg
from model.app_schema.user_schema import UserCreate, User


router = APIRouter(
    prefix="/file",
    tags=["file"],
    # dependencies=[Depends(get_db)],
    responses={404: {"description": "Not Found"}}
)

@router.post("/upload-pdf/")
async def add_pdf():
    return {"message":"This endpoint allows you upload your pdf"};
    
