from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from database.model_functions.country import Countrydb
from database.model_functions.state import Statedb

router = APIRouter()


@router.post("/state-list",name="statelist")
def getState(db:Session = Depends(get_db)):
    try:
        alldata = Statedb.read_all(db)
        return alldata
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/save-state",name="savestate")
def saveState(db:Session = Depends(get_db)):
    try:
        insetedData = Statedb.saveData(db)
        return insetedData
    except Exception as e:
        print(f"Exception error {e}")
