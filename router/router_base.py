from fastapi import APIRouter, FastAPI
from router.api import user_route

api_router = APIRouter()
# include the router
api_router.include_router(user_route.router, prefix="", tags=["users"])