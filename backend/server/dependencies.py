from fastapi import Header, HTTPException


# get token from header when request is made
async def get_header_token(token: str = Header(...)):
    if token != "pdf-reader-secret-token":
        raise HTTPException(status_code=400, detail="Invalid Token Provided")


# get token from query string
async def get_query_token(token: str):
    if token != "pdf-reader-secret-token":
        raise HTTPException(status_code=400, detail="Invalid Token Provided")
