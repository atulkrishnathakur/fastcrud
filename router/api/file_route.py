import os
from fastapi import APIRouter,Depends,status, File, UploadFile
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from database.model_functions.user import (read_all_user,saveUser,saveOrUpdateUser,
updateUser,deleteUser,readbyoperators)
import logging

router = APIRouter()

@router.post("/upload-file",name="uploadfile")
def uploadFile(file: UploadFile = File(...)):
    try:
        UPLOAD_DIRECTORY = "./uploads/" # Ensure the directory exists 
        os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
        file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        return {"info": f"file '{file.filename}' saved at '{file_location}'"}
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/upload-file-by-uploadfile",name="uploadfile")
def uploadFile(file:UploadFile):
    try:
        UPLOAD_DIRECTORY = "./uploads/" # Ensure the directory exists 
        os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
        file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        return {"info": f"file '{file.filename}' saved at '{file_location}'"}
    except Exception as e:
        print(f"Exception error {e}")