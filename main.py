from fastapi import FastAPI, Header, HTTPException

from core.router import router

app = FastAPI()

app.include_router(router)
