from database.model.user import User
from fastapi import Depends
from fastapi import status
from sqlalchemy import select
from sqlalchemy import insert
from database.dbconnection import engine
def read_all_user(db):
    try:
        # https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html
        #get all users by query
        #result = db.query(User).all()
        #return result

        # get all users by scalars
        #result = db.scalars(select(User))
        #result = db.scalars(select(User).order_by(User.id))
        #return result.all()

        #get all users by execute
        #result = db.execute(select(User).order_by(User.id))
        #return result.scalars().all()

        #get all users by select
        #stmt = select(User)
        #compile_stmt = stmt.compile(engine) # print the sql query
        #print(compile_stmt)
        #result = db.execute(stmt)
        #return result.scalars().all()

        stmt = select(User).where(User.firstname == 'Atul')
        compile_stmt = stmt.compile(engine)
        #print(compile_stmt)
        result = db.execute(stmt)
        return result.scalars().all()

    except Exception as e:
        print(f"Exception error{e}")

def saveUser(db):
    try:
        # https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
        
        """
        db.execute(
            insert(User),
            [
                {"id":5,"firstname":"Ram","secondname":"Thakur","email":"myeml3@yopmail.com","status":1},
                {"id":6,"firstname":"Balram","secondname":"Thakur","email":"myeml4@yopmail.com","status":1},
                {"id":7,"firstname":"Krishna","secondname":"Thakur","email":"myeml5@yopmail.com","status":1},
                {"id":8,"firstname":"Guru","secondname":"Thakur","email":"myeml6@yopmail.com","status":1}
            ]
        )
        db.commit()
        result = db.execute(select(User).order_by(User.id))
        return result.scalars().all()
        """
        
        """
        userdata = db.execute(
            insert(User).returning(User),
            [
                {"id":25,"firstname":"Ram","secondname":"Thakur","email":"myeml23@yopmail.com","status":1},
                {"id":26,"firstname":"Balram","secondname":"Thakur","email":"myeml24@yopmail.com","status":1},
                {"id":27,"firstname":"Krishna","secondname":"Thakur","email":"myeml25@yopmail.com","status":1},
                {"id":28,"firstname":"Guru","secondname":"Thakur","email":"myeml26@yopmail.com","status":1}
            ]
        )
        db.commit()
        return userdata.scalars().all()
        # returning() function return latest inserted users
        """
    except Exception as e:
        print(f"Exception erro{e}")