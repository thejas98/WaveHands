from fastapi import FastAPI,Request
import os
from dotenv import load_dotenv
from api import signconversion,registration
load_dotenv()

secret_key = os.environ.get("SECRET_KEY")
app = FastAPI()


app.include_router(signconversion.router_signconversion)
app.include_router(registration.router_registration)

@app.get("/test")
async def root():
    return {"message": "Hello Bigger Applications!"}