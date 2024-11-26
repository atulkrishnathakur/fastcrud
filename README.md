## How to create the virtual environment in python

-- If in ubuntu by default python3.10 installed but you want to use python3.12 version in linux then install python3.12 in ubuntu

```
atul@atul-Lenovo-G570:~$ cd fastcrud
atul@atul-Lenovo-G570:~/fastcrud$ python3.12 -m venv env
```

## how to activate the virtual environment

```
atul@atul-Lenovo-G570:~/fastcrud$ source env/bin/activate
(env) atul@atul-Lenovo-G570:~/fastcrud$
```

## How to check python version in virtual environment

```
(env) atul@atul-Lenovo-G570:~/fastcrud$ python --version
Python 3.12.7
```
Or

```
(env) atul@atul-Lenovo-G570:~/fastcrud$ python3 --version
Python 3.12.7
```

## How to check PIP version in python virtual environment

```
(env) atul@atul-Lenovo-G570:~/fastcrud$ pip --version
pip 24.2 from /home/atul/fastcrud/env/lib/python3.12/site-packages/pip (python 3.12)
```

or 

```
(env) atul@atul-Lenovo-G570:~/fastcrud$ pip3 --version
pip 24.2 from /home/atul/fastcrud/env/lib/python3.12/site-packages/pip (python 3.12)
```

## How to clone repository from github?

```
(env) atul@atul-Lenovo-G570:~$ git clone https://github.com/atulkrishnathakur/fastcrud.git
Cloning into 'fastcrud'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.
```
## How to generate requirements.txt in python?

```
(env) atul@atul-Lenovo-G570:~/fastcrud$ pip3 freeze > requirements.txt
```

## How to install fastapi

https://fastapi.tiangolo.com/tutorial/#install-fastapi

```
(env) atul@atul-Lenovo-G570:~/fastcrud$ pip install "fastapi[standard]"
```

## How to run uvicorn server

The command uvicorn main:app refers to:

1. main: the file main.py (the Python "module").
2. app: the object created inside of main.py with the line app = FastAPI().
3. --reload: make the server restart after code changes. Only use for development.

```
(env) atul@atul-Lenovo-G570:~/fastcrud$ uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/home/atul/fastcrud']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [5757] using WatchFiles
INFO:     Started server process [5759]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## How to install sqlalchemy ORM

```
(env) atul@atul-Lenovo-G570:~/fastcrud$ pip3 install sqlalchemy
```

## how to install psycopg2-binary?
```
(env) atul@atul-Lenovo-G570:~/fastcrud$ pip3 install psycopg2-binary
```

## How to install alembic to create migrations in fastapi?

```
(env) atul@atul-Lenovo-G570:~/fastcrud$ pip3 install alembic
```

Below command will create an alembic directory with necessary configuration files.

```
(env) atul@atul-Lenovo-G570:~/fastcrud$ alembic init alembic
```

## How to configure alembic.ini file?
You can see alembic.ini file outside of alembic directory. The alembic.ini file path is fastcrud/alembic.ini. 

```
sqlalchemy.url = postgresql://postgres:123456789@localhost:5432/fastcrud_db
```

## How to create database connection with sqlalchemy ORM?

1. create fastcrud/database directory
2. create the fastcrud/database/dbconnection.py
3. create the `fastcrud/database/__init__.py`
```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456789@localhost:5432/fastcrud_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

## Create the model directory for sqlalchemy ORM

1. create the database/model directory
2. create the `database/model/__init__.py` file
3. import the created model in `database/model/__init__.py` file

## set the env.py in alembic

1. import "from database.dbconnection import Base"
2. import "from database.model import *"
3. assign base metadata "target_metadata = Base.metadata"

```
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from database.dbconnection import Base # by atul

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None

from database.model import * # by atul
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

## How to create use model
1. create the model in fastcrud/database/model/user.py
```
from sqlalchemy import (BigInteger,Column,PrimaryKeyConstraint,Text,String,Integer,DateTime,
BigInteger,SmallInteger,func,UniqueConstraint,ForeignKey)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped
from database.dbconnection import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pkey'),
        UniqueConstraint('email', name='uix_email')
    )

    id: Mapped[BigInteger] = mapped_column('id',BigInteger,primary_key=True,autoincrement=True,nullable=False)
    firstname: Mapped[String] = mapped_column('first_name',String(255),nullable=False)
    secondname:Mapped[String] = mapped_column('second_name',String(255),nullable=True)
    email:Mapped[String] = mapped_column('email',String(255),unique=True,nullable=True)
    password:Mapped[String] = mapped_column('password',String(255),nullable=True)
    status:Mapped[SmallInteger] = mapped_column('status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")
    created_at:Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at:Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)
```
2. edit the `fastcrud/database/model/__init__.py` file
```
from .user import User
```
## Create migration by alembic
1. run the command
```
(env) atul@atul-Lenovo-G570:~/fastcrud$ alembic revision --autogenerate -m "Initial Migration"
```
2. manually review the migration file
```
"""Initial Migration

Revision ID: 6134c1b9c945
Revises: 
Create Date: 2024-11-06 10:29:18.994478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6134c1b9c945'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('second_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True, comment='1=Active,0=Inactive'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email', name='uix_email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
```

3. migrate (upgrade) the migration file
```
(env) atul@atul-Lenovo-G570:~/fastcrud$ alembic upgrade head
```

4. Check database for the newly created table

## What is router in FastAPI?
Reference: https://fastapi.tiangolo.com/reference/apirouter/
1. Router helps you define endpoints and organize your API routes in a structured way.
2. In FastAPI, a router is essentially a way to modularize your application by grouping related endpoints.
3. FastAPI router work same as controller of other technoloy
## Route directory structure
1. create `fastcrud/router/__init__.py`
2. create `fastcrud/router/api/__init__.py`
3. create fastcrud/router/api/user_router.py
```
from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/get-user",name="getuser")
def getUser():
    try:
        return "Hello"
    except ValueError as e:
        pass
```
4. create fastcrud/router/router_base.py
```
from fastapi import APIRouter, FastAPI
from router.api import user_route

api_router = APIRouter()
# include the router
api_router.include_router(user_route.router, prefix="", tags=["users"])
```
5. edit the fastcrud/main.py
```
from fastapi import FastAPI
from fastapi import FastAPI,Depends, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from router.router_base import api_router

app = FastAPI()

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(DEBUG=True)
    include_router(app)
    return app

app = start_application()
```
6. Run the uvicorn server and test

## sqlalchemy database session
1. create fastcrud/database/session.py
```
from .dbconnection import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```
## What is yield
reference: https://www.w3schools.com/python/ref_keyword_yield.asp
1. yield is a keyword
2. yield work as return but yield donot stop code execution


## hashing 
1. It is for hashed password
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-passlib

```
(env) atul@atul-Lenovo-G570:~/fastcrud$ pip3 install "passlib[bcrypt]"
```

# How to select data from table using sqlalchemy
Reference: https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html
1. edit the /home/atul/fastcrud/router/api/user_route.py

```
from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from database.model_functions.user import (read_all_user,saveUser,saveOrUpdateUser,
updateUser,deleteUser,readbyoperators)

router = APIRouter()

@router.post("/get-user",name="getuser")
def getUser(db:Session = Depends(get_db)):
    try:
        allUser = read_all_user(db)
        return allUser
    except Exception as e:
        print(f"Exception error {e}")

@router.post("/create-user",name="createuser")
def createUser(db:Session = Depends(get_db)):
    try:
        allUser = saveUser(db)
        return allUser
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/upsert-user",name="upsertuser")
def saverOrUpdateUser(db:Session = Depends(get_db)):
    try:
        allUser = saveOrUpdateUser(db)
        return allUser
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/update-user",name="updateuser")
def saverOrUpdateUser(db:Session = Depends(get_db)):
    try:
        allUser = updateUser(db)
        return allUser
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/delete-user",name="deleteuser")
def saverOrUpdateUser(db:Session = Depends(get_db)):
    try:
        allUser = deleteUser(db)
        return allUser
    except Exception as e:
        print(f"Exception error {e}")

@router.post("/select-user-by-operator",name="deleteuserbyoperator")
def selectuserbyoperatorfn(db:Session = Depends(get_db)):
    try:
        allUser = readbyoperators(db)
        return allUser
    except Exception as e:
        print(f"Exception error {e}")

```

2. create the fastcrud/database/model_functions/user.py
```
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
from fastapi.encoders import jsonable_encoder

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
        stmt = select(User)
        result = db.execute(stmt)
        data = result.all()
        #print(data[0][0].firstname) # manualy print firstname
        response_content = [
            {"first_name": user.User.firstname,
            'second_name':user.User.secondname,
            'email':user.User.email
            } for user in data]
        #print(response_content) # use to print content
        jsondata = jsonable_encoder(response_content)
        return jsondata

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
```

- in read_all_user funciton you can see to select all users
```
# https://docs.sqlalchemy.org/en/20/orm/queryguide/select.html
#get all users by query
result = db.query(User).all()
return result
```

- in read_all_user funciton you can see a new way to select all users
```
#get all users by scalar
result = db.scalars(select(User).order_by(User.id))
return result.all()
```

- in read_all_user funciton you can see a new way to select all users
- compile() function used to print sql query in terminal
```
#get all users by select
stmt = select(User)
compile_stmt = stmt.compile(engine) # print the sql query
print(compile_stmt)
result = db.execute(stmt)
return result.scalars().all()
```

- in read_all_user funciton you can see a new way to select all users using where clause
- compile() function used to print sql query in terminal
```
stmt = select(User).where(User.firstname == 'Atul')
compile_stmt = stmt.compile(engine)
#print(compile_stmt)
result = db.execute(stmt)
return result.scalars().all()
```
- In read_all_user function you can see a new way to select all user. Here we are not using scalars() function. Here we are make data using jsonable_encoder() function. In this way you can controller your data.

```
stmt = select(User)
result = db.execute(stmt)
data = result.all()
#print(data[0][0].firstname) # manualy print firstname
response_content = [
    {"first_name": user.User.firstname,
    'second_name':user.User.secondname,
    'email':user.User.email
    } for user in data]
#print(response_content) # use to print content
jsondata = jsonable_encoder(response_content)
return jsondata
```

- in saveUser() funciton you can see to insert data in database table
- You can save data in bulk

```
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
```

- in saveUser() funciton you can see to insert data in database table
- You can save data in bulk
- returning() function used to return latest inserted data
```
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
```

- in saveUser() funciton you can see to insert new way to insert data in database table
- Reference: https://docs.sqlalchemy.org/en/20/orm/session_basics.html#adding-new-or-existing-items

```
db_user = User(firstname="Atullll",secondname="Thakurrrr",email="myeml27@yopmail.com",status=1)
db.add(db_user)
db.commit()
db.refresh(db_user)
return db_user
```

- in updateUser() you can update data according to primary key in bulk. We have added primary key on id field. so data will be update according to id field.
- References: https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html 

```
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
```

- in updateUser() function you will see bindparam() function. It is used to update data in bulk. You can use dictionary key as argument of bindparam() function. 
- Reference: https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html 

```
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
```

- In updateUser() you can see new way to update record using where clause
- Reference: https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html

```
stmt = update(User).where(User.firstname.in_(["Ram Kumar","Krishna Thakur"])).values(secondname="Tha",email="ram@yopmail.com")
db.execute(stmt)
db.commit()
```

- Note: You can also check sqlalchemy 1.4 version if you have need from https://docs.sqlalchemy.org/en/14/orm/query.html


- In deleteUser() function you will see a way to delete data using where clause.
- References: https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html 
```
stmt = delete(User).where(User.email == "ram@yopmail.com")
db.execute(stmt)
db.commit()
```

- In deleteUser() function you will see a new way to delete data using where clause.
- References: https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html 

```
stmt = delete(User).where(User.id.in_([6,7]))
db.execute(stmt)
db.commit()
```

- In readbyoperators() function you will see to get value of field
```
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
```

- In readbyoperators() function you will see to get records using where clause.
```
stmt = select(User).where(User.id == 10)
result = db.execute(stmt)
return result.scalars().all()
```

- In readbyoperators() function you will see to get single record using one() function.
```
stmt = select(User).where(User.id == 10)
result = db.execute(stmt)
return result.scalars().one()
```

- In readbyoperators() function you will see to get single record using first() function.
```
stmt = select(User).where(User.id == 10)
result = db.execute(stmt)
return result.scalars().first()
```

- In readbyoperators() function you will see to get records using where clause with and_ .
- Reference: https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.and_

```
stmt = select(User).where(User.id == 10)
result = db.execute(stmt)
return result.scalars().all()
```

- In readbyoperators() function you will see to get records using multiple time where clause with and_ .
- Reference: https://docs.sqlalchemy.org/en/20/core/sqlelement.html#sqlalchemy.sql.expression.and_

```
stmt = select(User).where(and_(User.firstname == "Guru",User.email=="myeml81@yopmail.com")).where(User.id==34)
result = db.execute(stmt)
print(stmt.compile(engine)) # see query in terminal
return result.scalars().all()
```
- Note: You can learn more sql operators from https://docs.sqlalchemy.org/en/20/core 


- In text() function you can use queries to run

```
db.execute(text("TRUNCATE TABLE users;"))
db.execute(text("ALTER SEQUENCE users_id_seq RESTART WITH 1;"))
db.commit()
```

## postgresql data types in sqlalchemy
References: https://docs.sqlalchemy.org/en/20/dialects/postgresql.html 
```from sqlalchemy.dialects.postgresql import (
    ARRAY,
    BIGINT,
    BIT,
    BOOLEAN,
    BYTEA,
    CHAR,
    CIDR,
    CITEXT,
    DATE,
    DATEMULTIRANGE,
    DATERANGE,
    DOMAIN,
    DOUBLE_PRECISION,
    ENUM,
    FLOAT,
    HSTORE,
    INET,
    INT4MULTIRANGE,
    INT4RANGE,
    INT8MULTIRANGE,
    INT8RANGE,
    INTEGER,
    INTERVAL,
    JSON,
    JSONB,
    JSONPATH,
    MACADDR,
    MACADDR8,
    MONEY,
    NUMERIC,
    NUMMULTIRANGE,
    NUMRANGE,
    OID,
    REAL,
    REGCLASS,
    REGCONFIG,
    SMALLINT,
    TEXT,
    TIME,
    TIMESTAMP,
    TSMULTIRANGE,
    TSQUERY,
    TSRANGE,
    TSTZMULTIRANGE,
    TSTZRANGE,
    TSVECTOR,
    UUID,
    VARCHAR,
)
```

## How to use Sequences/SERIAL/IDENTITY in sqlalchemy
References: https://docs.sqlalchemy.org/en/20/dialects/postgresql.html


## How to logging 
References:https://docs.python.org/3/howto/logging.html 


## select data from inner join, left join and use jsonable_encoder
- create a file database/model_functions/state.py
- join() function used as inner join

```
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
```
- in read_all function you can see to join two modle
```
stmt = select(State,Country).join(Country, State.countries_id == Country.id) # join() used for inner join
result = db.execute(stmt) 
data = result.all() # Here we can not use scalars() because scalars() use with only one object. Here it return object in tuple. You can check by print.
#print(data)
response_content = [{"state_id":state.id,"country_id":state.countries_id,"country_name": country.countryname, "state_name": state.statename} for state, country in data]
#print(response_content)
jsondata = jsonable_encoder(response_content)
return jsondata
```
- in read_all function you can see to join two modle and select specific fields
```
stmt = select(State.id,State.statename,Country.countryname).join(Country, State.countries_id == Country.id) # join() used for inner join
result = db.execute(stmt) 
data = result.all() # It return tuple with values only
#print(data)
response_content = [{"state_id":stateid,"country_name":countryname, "state_name":statename} for stateid, statename,countryname in data] # it return values according to select() field respectively.
#print(response_content)
jsondata = jsonable_encoder(response_content)
return jsondata
```
- in read_all function you can see `isouter=True`
```
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
```


## How to use IDENTITY in sqlalchemy model for postgresql database
Reference: https://docs.sqlalchemy.org/en/20/dialects/postgresql.html 
1. create database/model/city.py
```
from sqlalchemy import (BigInteger,Column,PrimaryKeyConstraint,Text,String,Integer,DateTime,
BigInteger,SmallInteger,func,UniqueConstraint,ForeignKey,Identity)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped
from database.dbconnection import Base

class City(Base):
    __tablename__ = 'cities'
    __table_args__ = (PrimaryKeyConstraint('id', name='cities_pkey'),)

    id: Mapped[BigInteger] = mapped_column('id',BigInteger,Identity(start=1, cycle=False),primary_key=True,nullable=False)
    cityname: Mapped[String] = mapped_column('city_name',String(255),nullable=True)
    state_id:Mapped[BigInteger] = mapped_column('state_id',BigInteger,ForeignKey('countries.id'),nullable=True)
    status:Mapped[SmallInteger] = mapped_column('status',SmallInteger,nullable=True,default=1,comment="1=Active,0=Inactive")
    created_at:Mapped[DateTime] = mapped_column('created_at',DateTime, nullable=True, server_default=func.now())
    updated_at:Mapped[DateTime] = mapped_column('updated_at',DateTime,nullable=True)
```

2. You can check migration for City model
```
"""initial city migration

Revision ID: 885729b6aafe
Revises: 83ade7a29406
Create Date: 2024-11-22 11:02:45.887197

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '885729b6aafe'
down_revision: Union[str, None] = '83ade7a29406'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('id', sa.BigInteger(), sa.Identity(always=False, start=1, cycle=False), nullable=False),
    sa.Column('city_name', sa.String(length=255), nullable=True),
    sa.Column('state_id', sa.BigInteger(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True, comment='1=Active,0=Inactive'),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['state_id'], ['countries.id'], ),
    sa.PrimaryKeyConstraint('id', name='cities_pkey')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cities')
    # ### end Alembic commands ###
```

# for left join or full joi check the url
Reference: https://docs.sqlalchemy.org/en/20/tutorial/data_select.html

## loguru package for logging in python
Reference: https://loguru.readthedocs.io/en/stable/
Reference: https://pypi.org/project/loguru/

- install loguru
```
(env) atul@atul-Lenovo-G570:~/fastcrud$ pip3 install loguru
Collecting loguru
  Downloading loguru-0.7.2-py3-none-any.whl.metadata (23 kB)
Downloading loguru-0.7.2-py3-none-any.whl (62 kB)
Installing collected packages: loguru
Successfully installed loguru-0.7.2
```