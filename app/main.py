from fastapi import FastAPI
from starlette.responses import RedirectResponse
from crud import router as BookRouter

app = FastAPI()

@app.get("/",tags=["Root"])
async def read_root():
    return RedirectResponse("/docs/")

app.include_router(BookRouter, tags=["Library"], prefix="/library")


