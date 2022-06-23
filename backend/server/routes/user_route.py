from fastapi import APIRouter, Depends, HTTPException
from typing import Any, Optional
from dependencies import get_header_token
from fastapi.security import HTTPBearer
from model.app_schema.user_schema import UserCreate, UserBase

token_auth_scheme: HTTPBearer = HTTPBearer()

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_header_token)],
    responses={404: {"description": "Not Found"}}
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}


@router.get("/")
async def home(item: UserCreate) ->Any:
    if not item:
        raise HTTPException(status_code = 404, detail=f"{item} should be provided")
    return {**item.dict()}


@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}

@router.get("/addition/add-number")
async def addNumbers(num_one: int, num_two: int) ->int:
    return num_one + num_two

## optional query string
@router.get("/items/{item_id}")
async def getItems(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query_string": q}