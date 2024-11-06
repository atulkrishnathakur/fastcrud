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

## Create the model for sqlalchemy ORM?

1. create the database/model directory
2. create the database/model/__init__.py file
3. import the created model in database/model/__init__.py file

