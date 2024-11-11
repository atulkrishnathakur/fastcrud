from database.model.user import User
from fastapi import Depends
from fastapi import status
from sqlalchemy import select
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