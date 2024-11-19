from database.model.state import State
from fastapi import Depends
from fastapi import status
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import text
from sqlalchemy import bindparam
from sqlalchemy import and_
from database.dbconnection import engine
from sqlalchemy.dialects.sqlite import insert as sql_upsert
from passlib.context import CryptContext
import random
from datetime import datetime

class Statedb:
    @staticmethod
    def read_all(db):
        try:
            stmt = select(State)
            result = db.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print(f"Exception error{e}")
    
    @staticmethod
    def saveData(db):
        try:
            #https://docs.sqlalchemy.org/en/20/orm/session_basics.html#adding-new-or-existing-items
            reqstatename = "Bihar"
            dbmodel = State(statename=reqstatename,status=1,countries_id=1)
            db.add(dbmodel)
            db.commit()
            db.refresh(dbmodel)
            return dbmodel
        except Exception as e:
            print(f"Exception error{e}")