from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from database.model_functions.country import Countrydb

router = APIRouter()


@router.post("/country-list",name="countrylist")
def getCountry(db:Session = Depends(get_db)):
    try:
        alldata = Countrydb.read_all(db)
        return alldata
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/save-country",name="savecountry")
def createUser(db:Session = Depends(get_db)):
    try:
        insetedData = Countrydb.saveData(db)
        return insetedData
    except Exception as e:
        print(f"Exception error {e}")

@router.post("/update-country",name="updatecountry")
def createCountry(db:Session = Depends(get_db)):
    try:
        updatedData = Countrydb.updateData(db)
        return updatedData
    except Exception as e:
        print(f"Exception error {e}")

@router.post("/delete-country",name="deletecountry")
def deleteCountry(db:Session = Depends(get_db)):
    try:
        deletedData = Countrydb.deleteCountry(db)
        return deletedData
    except Exception as e:
        print(f"Exception error {e}")
