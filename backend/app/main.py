from typing import Annotated
from fastapi import Body, FastAPI
from .api.routes import players, host

app = FastAPI()
app.include_router(players.router)
app.include_router(host.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Main Page!"}



