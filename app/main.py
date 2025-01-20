from fastapi import FastAPI
from api.router import api_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Russian Roulette",
    description="Russian Roulette based on Dong Size",
)

app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)