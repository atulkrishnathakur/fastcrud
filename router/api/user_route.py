from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/get-user",name="getuser")
def getUser():
    try:
        pass
    except ValueError as e:
        pass