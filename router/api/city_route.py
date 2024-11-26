from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from database.model_functions.country import Countrydb
from database.model_functions.state import Statedb
from database.model_functions.city import Citydb

router = APIRouter()

@router.post("/city-list",name="citylist")
def getCity(db:Session = Depends(get_db)):
    try:
        alldata = Citydb.read_all(db)
        return alldata
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/save-city",name="savecity")
def saveCity(db:Session = Depends(get_db)):
    try:
        insetedData = Citydb.saveData(db)
        return insetedData
    except Exception as e:
        print(f"Exception error {e}")

@router.post("/update-city",name="updatecity")
def updateUser(db:Session = Depends(get_db)):
    try:
        updatedData = Citydb.updateData(db)
        return updatedData
    except Exception as e:
        print(f"Exception error {e}")
