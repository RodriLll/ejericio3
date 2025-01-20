from api.russian_roulette import router as russian_roulette_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(russian_roulette_router, prefix="/russian_roulette", tags=["Russian Roulette"])
