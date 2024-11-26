from database.model.state import State
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
from fastapi.encoders import jsonable_encoder

class Statedb:
    @staticmethod
    def read_all(db):
        try:
            '''
            stmt = select(State,Country).join(Country, State.countries_id == Country.id) # join() used for inner join
            result = db.execute(stmt) 
            data = result.all() # Here we can not use scalars() because scalars() use with only one object. Here it return object in tuple. You can check by print.
            #print(data)
            response_content = [{"state_id":state.id,"country_id":state.countries_id,"country_name": country.countryname, "state_name": state.statename} for state, country in data]
            #print(response_content)
            jsondata = jsonable_encoder(response_content)
            return jsondata
            '''
            '''
            stmt = select(State.id,State.statename,Country.countryname).join(Country, State.countries_id == Country.id) # join() used for inner join
            result = db.execute(stmt) 
            data = result.all() # It return tuple with values only
            #print(data)
            response_content = [{"state_id":stateid,"country_name":countryname, "state_name":statename} for stateid, statename,countryname in data] # it return values according to select() field respectively.
            #print(response_content)
            jsondata = jsonable_encoder(response_content)
            return jsondata
            '''
            
            '''
            stmt = select(State.id,State.statename,Country.countryname).join(Country, State.countries_id == Country.id) # join() used for inner join
            result = db.execute(stmt) 
            data = result.all() # It return tuple with values only
            #print(data)
            response_content = [{"state_id":stateid,"country_name":countryname, "state_name":statename} for stateid, statename,countryname in data] # it return values according to select() field respectively.
            #print(response_content)
            jsondata = jsonable_encoder(response_content)
            return jsondata
            '''
            
            # left join and full join reference: https://docs.sqlalchemy.org/en/20/tutorial/data_select.html
            stmt = select(State.id,State.statename,Country.countryname).join(Country, State.countries_id == Country.id, isouter=True) # join() used for inner join
            result = db.execute(stmt) 
            print(stmt.compile(engine))
            data = result.all() # It return tuple with values only
            print(data)
            response_content = [{"state_id":stateid,"country_name":countryname, "state_name":statename} for stateid, statename,countryname in data] # it return values according to select() field respectively.
            print(response_content)
            jsondata = jsonable_encoder(response_content)
            return jsondata

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