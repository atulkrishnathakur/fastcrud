from database.model.state import State
from database.model.country import Country
from database.model.city import City
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
from fastapi.encoders import jsonable_encoder

class Citydb:
    @staticmethod
    def read_all(db):
        try:
            '''
            stmt = select(City,State).join(City, City.state_id == State.id) # join() used for inner join
            result = db.execute(stmt) 
            data = result.all() # Here we can not use scalars() because scalars() use with only one object. Here it return object in tuple. You can check by print.
            #print(data)
            response_content = [{"city_id":city.id,"state_id":city.state_id,"state_name": state.statename} for city, state in data]
            #print(response_content)
            jsondata = jsonable_encoder(response_content)
            return jsondata
            '''

            '''
            stmt = select(City.id,City.cityname,State.statename).join(City, State.id == City.state_id) # join() used for inner join
            result = db.execute(stmt) 
            data = result.all() # It return tuple with values only
            #print(data)
            response_content = [{"city_id":cityid,"city_name":cityname, "state_name":statename} for cityid, cityname,statename in data] # it return values according to select() field respectively.
            #print(response_content)
            jsondata = jsonable_encoder(response_content)
            return jsondata
            '''

            # left join and full join reference: https://docs.sqlalchemy.org/en/20/tutorial/data_select.html
            stmt = select(City.id,City.cityname,State.statename).join(City, City.state_id == State.id,isouter=True) # isouter=True used for inner join
            result = db.execute(stmt)
            print(stmt.compile(engine))
            data = result.all() # It return tuple with values only
            #print(data)
            response_content = [{"city_id":cityid,"city_name":cityname, "state_name":statename} for cityid, cityname,statename in data] # it return values according to select() field respectively.
            #print(response_content)
            jsondata = jsonable_encoder(response_content)
            return jsondata
            
        except Exception as e:
            print(f"Exception error{e}")
    
    @staticmethod
    def saveData(db):
        try:
            #https://docs.sqlalchemy.org/en/20/orm/session_basics.html#adding-new-or-existing-items
            reqcityname = "Patna"
            dbmodel = City(cityname=reqcityname,status=1,state_id=1)
            db.add(dbmodel)
            db.commit()
            db.refresh(dbmodel)
            return dbmodel
        except Exception as e:
            print(f"Exception error{e}")


    @staticmethod
    def updateData(db):
        try:
            # https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
            # It will be automatically update according to Id because primary key added on Id
            # It means it will be update according to primary key
            db.execute(
                update(City),
                [
                    {"id":1,"city_name":"Patna u","state_id":1,"status":1},
                    {"id":2,"city_name":"Arrah u","state_id":1,"status":1},
                    {"id":3,"city_name":"Buxar u","state_id":1,"status":1},
                    {"id":4,"city_name":"Bihta u","state_id":1,"status":1}
                ]
            )
            db.commit()
        except Exception as e:
            print(f"Exception error{e}")