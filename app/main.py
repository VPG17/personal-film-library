from fastapi import FastAPI
from app.routers import search as search_module

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(search_module.router)