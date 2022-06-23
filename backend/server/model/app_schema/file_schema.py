from typing import List, Optional

from pydantic import BaseModel


class FileBase(BaseModel):
    name:str


class FileCreate(FileBase):
    pass


class File(FileBase):
    id: int

    class Config:
        orm_mode = True
