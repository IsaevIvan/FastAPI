from fastapi import FastAPI
from fastapi.responses import FileResponse
import logging

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.get("/custom")
async def read_custom_message():
    return {"message":"This is a custom message"}
