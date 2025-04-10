from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.logger import logger

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("../index.html")

@app.get("/custom")
async def read_custom_message():
    logger.info(f"Redirect to page Custom")
    return {"message":"This is a custom message"}
