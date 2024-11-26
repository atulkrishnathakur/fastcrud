from fastapi import APIRouter, FastAPI
from router.api import user_route
from router.api import country_route,state_route,city_route

api_router = APIRouter()
# include the router
api_router.include_router(user_route.router, prefix="", tags=["users"])
api_router.include_router(country_route.router, prefix="", tags=["country"])
api_router.include_router(state_route.router, prefix="", tags=["state"])
api_router.include_router(city_route.router, prefix="", tags=["city"])