from fastapi import FastAPI

from core.router import router

app = FastAPI()

app.include_router(router)
