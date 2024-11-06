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
3. create the fastcrud/database/__init__.py
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
2. create the database/model/__init__.py file
3. import the created model in database/model/__init__.py file

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
2. edit the fastcrud/database/model/__init__.py file
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
