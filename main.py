from fastapi import FastAPI
from fastapi import FastAPI,Depends, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from router.router_base import api_router
from config.static_mount import mount_uploaded_files
#app = FastAPI()

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(DEBUG=True)
    include_router(app)
    mount_uploaded_files(app)
    return app

app = start_application()