from schemas.base import CamelModel
from pydantic import Field
from enum import Enum

class BulletType(Enum):
    SILVER = "SILVER"
    GOLD = "GOLD"
    DIAMOND = "DIAMOND"

class RussianRouletteInput(CamelModel):
    bullet_type: BulletType = Field(..., description="Type of bullet", examples=["SILVER", "GOLD", "DIAMOND"])
    dong_size: float = Field(..., ge=0, le=2, description="Size of your dong in centimeters", examples=[0.1, 0.2, 0.3])

class RussianRouletteOutput(CamelModel):
    message: str = Field(..., description="Russian Roulette message", examples=["Sobreviviste"])