from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_header_token

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    # dependencies=[Depends(get_header_token)],
    responses={404: {"description": "Not Found"}}
)



@router.get("/")
async def home():
    return {"message": fake_items_db}
