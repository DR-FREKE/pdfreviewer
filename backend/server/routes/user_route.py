from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_header_token

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_header_token)],
    responses={404: {"description": "Not Found"}}
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def home():
    return {"message": fake_items_db}


@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}
