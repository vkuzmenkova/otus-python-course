from fastapi import FastAPI
import csv
from user import User, UserOut
import uuid

app = FastAPI()


@app.get("/")
def root():
    return {'hello': 'world!'}


@app.get("/ping/")
def ping():
    return {"message": "pong"}





