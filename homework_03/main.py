from fastapi import FastAPI
import csv
import uuid
from item import ItemIn, Item
from typing import Optional, Dict

app = FastAPI()

USER_DICT = {}
ITEMS_DICT = {}


@app.get("/")
def root(name: str = "World"):
    return {"Hello": name}


@app.get("/ping/", summary="sends \"pong\" in response")
def ping():
    return {"message": "pong"}


@app.post("/items/create", summary="creates item", response_model=Item)
def create_item(input_item: ItemIn):
    item = Item(id=str(uuid.uuid4()), **input_item.dict())
    ITEMS_DICT[item.id] = item
    return item


@app.get("/items/item")
def get_item(id: str):
    return ITEMS_DICT[id]
