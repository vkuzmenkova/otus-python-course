from fastapi import FastAPI, exceptions
import uuid
from item import ItemBase, ItemIn, Item
from datetime import datetime
from typing import Dict, List

app = FastAPI()

ITEMS_DICT: Dict[str, Item] = {}


def id_validation(input_id: str):
    if input_id not in ITEMS_DICT.keys():
        raise exceptions.HTTPException(
            404,
            {"message": f"No item with id = {input_id}."}
        )


@app.get("/")
def root(name: str = "World"):
    return {"Hello": name}


@app.get("/ping/", summary="sends \"pong\" in response")
def ping():
    return {"message": "pong"}


@app.post("/items/create", summary="creates item", tags=["Items"],
          response_model=Item)
def create_item(input_item: ItemBase):
    item = Item(id=str(uuid.uuid4()), created_at=datetime.now(),
                last_change_at=datetime.now(), **input_item.dict())
    ITEMS_DICT[item.id] = item
    return item


@app.get("/items/{item_id}", response_model=Item, tags=["Items"],
         summary="gets item by id")
def get_item(input_id: str):
    id_validation(input_id)
    return ITEMS_DICT[input_id]


@app.put("/items/update", summary="updates item description by id",
         tags=["Items"], response_model=Item)
def update_item(item: ItemIn):
    id_validation(item.id)

    ITEMS_DICT[item.id].name = item.name
    ITEMS_DICT[item.id].country_of_origin = item.country_of_origin
    ITEMS_DICT[item.id].weight = item.weight
    ITEMS_DICT[item.id].entity = item.entity
    ITEMS_DICT[item.id].last_change_at = datetime.now()

    return ITEMS_DICT[item.id]


@app.delete("/items/delete", summary="deletes item by id", tags=["Items"])
def get_item(input_id: str):
    id_validation(input_id)
    del ITEMS_DICT[input_id]
    return {"message": f"Item with id = {input_id} deleted."}


@app.get("/items", summary="gets all items", tags=["Items"],
         response_model=List[Item])
def get_all_items():
    tmp_list = []
    for key in ITEMS_DICT.keys():
        tmp_list.append(ITEMS_DICT[key])
    return tmp_list
