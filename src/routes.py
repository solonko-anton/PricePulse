from typing import TYPE_CHECKING
from fastapi import APIRouter
from src.api.olx.api import router as olx_router

def get_apps_router():
    router = APIRouter()
    router.include_router(olx_router)
    return router
