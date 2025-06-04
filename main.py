from fastapi import FastAPI
from api.router import router as user_router

app = FastAPI()

app.include_router(user_router)
