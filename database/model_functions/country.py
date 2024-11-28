from database.model.country import Country
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

class Countrydb:
    @staticmethod
    def read_all(db):
        try:
            stmt = select(Country)
            result = db.execute(stmt)
            return result.scalars().all()
        except Exception as e:
            print(f"Exception error{e}")
    
    @staticmethod
    def saveData(db):
        try:
            #https://docs.sqlalchemy.org/en/20/orm/session_basics.html#adding-new-or-existing-items
            reqcontryname = "Isarail"
            dbmodel = Country(countryname=reqcontryname,status=1)
            db.add(dbmodel)
            db.commit()
            db.refresh(dbmodel)
            return dbmodel
        except Exception as e:
            print(f"Exception error{e}")


    @staticmethod
    def updateData(db):
        try:
            '''
            # https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
            # It will be automatically update according to Id because primary key added on Id
            # It means it will be update according to primary key
            # here cityname, id, state_id key uses from city model
            db.execute(
                update(Country),
                [
                    {"id":1,"countryname":"India u","status":1},
                    {"id":2,"countryname":"Japan u","status":1},
                    {"id":3,"countryname":"Srilanka u","status":1},
                    {"id":4,"countryname":"Isarail u","status":1}
                ]
            )   
            db.commit()
            '''
            
            '''
            db.connection().execute(
                update(Country).where(Country.countryname== bindparam("c_name")).values(
                    countryname=bindparam("new_country_name")
                ),
                [
                    {"c_name":"India u","new_country_name":"India uUUU"},
                    {"c_name":"Japan u","new_country_name":"Japan uUUU"},
                    {"c_name":"Srilanka u","new_country_name":"Srilanka uUUUUU"},
                    {"c_name":"Isarail u","new_country_name":"Isarail uUUU"}
                ]
            )
            db.commit()
            '''

            stmt = update(Country).where(Country.countryname.in_(["India uUUU","Japan uUUU"])).values(countryname="India u",status=0)
            compiled_stmt = stmt.compile(engine, compile_kwargs={"literal_binds": True})
            print(compiled_stmt) # print sql
            db.execute(stmt)
            db.commit()
            
        except Exception as e:
            print(f"Exception error{e}")

    @staticmethod
    def deleteCountry(db):
        try:
            '''
            # https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
            stmt = delete(Country).where(Country.id == 1) # foreign key voilation error found
            db.execute(stmt)
            db.commit()
            '''


            '''
            stmt = delete(Country).where(Country.id == 100)
            db.execute(stmt)
            db.commit()
            '''
            
        except Exception as e:
            print(f"Exception error{e}")
