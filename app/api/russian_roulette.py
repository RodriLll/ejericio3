from fastapi import APIRouter, Body
from schemas.russian_roulette import RussianRouletteInput, RussianRouletteOutput
from services.russian_roulette import RussianRouletteService

router = APIRouter()

@router.post("/shoot")
def shoot(payload: RussianRouletteInput = Body(...)) -> RussianRouletteOutput:
    print(payload.model_dump())
    return RussianRouletteService.shoot(payload.model_dump())