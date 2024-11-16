from database.model.user import User
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

def read_all_user(db):
    try:
        """
        # https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html
        #get all users by query
        result = db.query(User).all()
        return result
        """
        
        """
        # get all users by scalar
        result = db.scalars(select(User).order_by(User.id))
        return result.all()
        """
        
        """
        #get all users by execute
        result = db.execute(select(User).order_by(User.id))
        return result.scalars().all()
        """
        """
        #get all users by select
        stmt = select(User)
        compile_stmt = stmt.compile(engine) # print the sql query
        print(compile_stmt)
        result = db.execute(stmt)
        return result.scalars().all()
        """

        """
        stmt = select(User).where(User.firstname == 'Atul')
        compile_stmt = stmt.compile(engine)
        #print(compile_stmt)
        result = db.execute(stmt)
        return result.scalars().all()
        """
    except Exception as e:
        print(f"Exception error{e}")

def saveUser(db):
    try:
        """
        db.execute(text("TRUNCATE TABLE users;"))
        db.execute(text("ALTER SEQUENCE users_id_seq RESTART WITH 1;"))
        db.commit()
        """
       
        """
         # https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
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
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
        userdata = db.execute(
            insert(User).returning(User),
            [
                {"firstname":"Ram","secondname":"Thakur","email":f"myeml{random.randrange(1,100)}@yopmail.com","password":pwd_context.hash('12345'),"status":1},
                {"firstname":"Balram","secondname":"Thakur","email":f"myeml{random.randrange(1,100)}@yopmail.com","password":pwd_context.hash('12345'),"status":1},
                {"firstname":"Krishna","secondname":"Thakur","email":f"myeml{random.randrange(1,100)}@yopmail.com","password":pwd_context.hash('12345'),"status":1},
                {"firstname":"Guru","secondname":"Thakur","email":f"myeml{random.randrange(1,100)}@yopmail.com","password":pwd_context.hash('12345'),"status":1}
            ]
        )
        db.commit()
        return userdata.scalars().all()
        
        # returning() function return latest inserted users
        """

        """
        #https://docs.sqlalchemy.org/en/20/orm/session_basics.html#adding-new-or-existing-items
        db_user = User(firstname="Atullll",secondname="Thakurrrr",email="myeml27@yopmail.com",status=1)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
        """
    except Exception as e:
        print(f"Exception erro{e}")
        db.rollback()


def saveOrUpdateUser(db):
    try:
        pass
        # Explain it again
    except Exception as e:
        print(f"Exception erro{e}")


def updateUser(db):
    try:
        '''
        # https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
        # It will be automatically update according to Id because primary key added on Id
        # It means it will be update according to primary key
        db.execute(
            update(User),
            [
                {"id":5,"firstname":"Ram u","secondname":"Thakur","email":"myeml1@yopmail.com","status":1},
                {"id":6,"firstname":"Balram u","secondname":"Thakur","email":"myeml2@yopmail.com","status":1},
                {"id":7,"firstname":"Krishna u","secondname":"Thakur","email":"myeml3@yopmail.com","status":1},
                {"id":8,"firstname":"Guru u","secondname":"Thakur","email":"myeml4@yopmail.com","status":1}
            ]
        )
        db.commit()
        '''


        """
        # https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
        # Bulk UPDATE statement with multiple parameter sets
        # If you do not usd bindparam then it you can use actual field of database table
        db.connection().execute(
            update(User).where(User.firstname== bindparam("u_fname")).values(
                firstname=bindparam("firstname"),
                secondname=bindparam("secondname"),
                email=bindparam("email"),
                status=bindparam("status")
            ),
            [
                {"u_fname":"Ram u","firstname":"Ram Kumar","secondname":"Thakur","email":"myeml11@yopmail.com","status":1},
                {"u_fname":"Balram u","firstname":"Krishna Kumar","secondname":"Thakur","email":"myeml21@yopmail.com","status":0},
                {"u_fname":"Krishna u","firstname":"Balram Kumar","secondname":"Thakur","email":"myeml31@yopmail.com","status":1},
                {"u_fname":"Guru u","firstname":"Atul Kumar","secondname":"Thakur","email":"myeml41@yopmail.com","status":1}
            ]
        )
        db.commit()
        """

        """
        # https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
        stmt = update(User).where(User.firstname.in_(["Ram Kumar","Krishna Thakur"])).values(secondname="Tha",email="ram@yopmail.com")
        db.execute(stmt)
        db.commit()
        """
 
        # You can also check sqlalchemy 1.4 from https://docs.sqlalchemy.org/en/14/orm/query.html 

    except Exception as e:
        print(f"Exception erro{e}")
        db.rollback()

def deleteUser(db):
    try:
        """
        # https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html

        stmt = delete(User).where(User.email == "ram@yopmail.com")
        db.execute(stmt)
        db.commit()
        """
        
        """
        # https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html
        stmt = delete(User).where(User.id.in_([6,7]))
        db.execute(stmt)
        db.commit()
        """
    except Exception as e:
        print(f"Exception erro{e}")
        db.rollback()

def readbyoperators(db):
    try:

        """
        stmt = select(User)
        result = db.execute(stmt)
        usersArr = result.scalars().all()
        userObj = usersArr[0]
        fname = userObj.firstname
        sname = userObj.secondname
        email = userObj.email
        created_at = userObj.created_at
        mydate = created_at.date()
        myyear = created_at.year
        mymonth = created_at.month
        myday = created_at.day
        mytime = created_at.time()
        myhour = created_at.time().hour
        myminutes = created_at.time().minute
        mysecond = created_at.time().second
        mymiliseconds = created_at.time().microsecond
        formatted_date = created_at.strftime("%m/%d/%Y")
        dayname = created_at.strftime("%A") # Saturday # https://www.w3schools.com/python/python_datetime.asp
        return formatted_date
        """
        '''
        stmt = select(User).where(User.id == 10)
        result = db.execute(stmt)
        return result.scalars().all()
        '''

        '''
        # get one record in object using one function
        stmt = select(User).where(User.id == 10)
        result = db.execute(stmt)
        return result.scalars().one()
        '''

        '''
        # get one record in object using first
        stmt = select(User).where(User.id == 10)
        result = db.execute(stmt)
        return result.scalars().first()
        '''
        
        """
        # https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.and_
        stmt = select(User).where(and_(User.firstname == "Krishna", User.email == "myeml62@yopmail.com"))
        result = db.execute(stmt)
        #print(stmt.compile(engine)) # see sql in terminal
        return result.scalars().all()
        """

        """
        # https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.and_
        stmt = select(User).where(and_(User.firstname == "Guru",User.email=="myeml81@yopmail.com")).where(User.id==34)
        result = db.execute(stmt)
        print(stmt.compile(engine)) # see query in terminal
        return result.scalars().all()
        """
    except Exception as e:
        pass