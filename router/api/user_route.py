from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from database.model_functions.user import read_all_user,saveUser

router = APIRouter()

@router.post("/get-user",name="getuser")
def getUser(db:Session = Depends(get_db)):
    try:
        allUser = read_all_user(db)
        return allUser
    except Exception as e:
        print(f"Exception error {e}")

@router.post("/create-user",name="createuser")
def createUser(db:Session = Depends(get_db)):
    try:
        allUser = saveUser(db)
        return allUser
    except Exception as e:
        print(f"Exception error {e}")