from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from database.model_functions.user import read_all_user,saveUser,saveOrUpdateUser,updateUser,deleteUser

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


@router.post("/upsert-user",name="upsertuser")
def saverOrUpdateUser(db:Session = Depends(get_db)):
    try:
        allUser = saveOrUpdateUser(db)
        return allUser
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/update-user",name="updateuser")
def saverOrUpdateUser(db:Session = Depends(get_db)):
    try:
        allUser = updateUser(db)
        return allUser
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/delete-user",name="deleteuser")
def saverOrUpdateUser(db:Session = Depends(get_db)):
    try:
        allUser = deleteUser(db)
        return allUser
    except Exception as e:
        print(f"Exception error {e}")
