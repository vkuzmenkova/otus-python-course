from fastapi import FastAPI, exceptions, status
import uuid
from item import ItemBase, ItemIn, Item
from datetime import datetime
from typing import Dict, List

app = FastAPI()


@app.get("/")
def root(name: str = "dub-dub"):
    return {"Wubba Lubba": name}


@app.get("/ping/", summary="sends \"pong\" in response")
def ping():
    return {"message": "pong"}


"""
=========================ITEMS==================================
"""
ITEMS_DICT: Dict[str, Item] = {}


def id_validation(input_id: str):
    if input_id not in ITEMS_DICT.keys():
        raise exceptions.HTTPException(
            404,
            {"message": f"No item with id = {input_id}."}
        )


@app.post("/item",
          summary="creates an item",
          tags=["Items"],
          response_model=Item,
          status_code=status.HTTP_201_CREATED
          )
def create_item(input_item: ItemBase):
    """
    Create an item with all the information:
    - **name**: each item must have a name
    - **country_of_origin**: country code, e.g. "UK"
    - **count**: number of items in store, must be integer >=0
    - **weight**: must be > 0

    **id**, **created_at**, **last_change_at** are filled automatically.
    """
    item = Item(id=str(uuid.uuid4()), created_at=datetime.now(),
                last_change_at=datetime.now(), **input_item.dict())
    ITEMS_DICT[item.id] = item
    return item


@app.get("/item/{item_id}",
         response_model=Item,
         tags=["Items"],
         summary="gets an item by id")
def get_item(input_id: str):
    id_validation(input_id)
    return ITEMS_DICT[input_id]


@app.get("/items",
         summary="gets all items in store",
         tags=["Items"],
         response_model=List[Item])
def get_all_items():
    tmp_list = []
    for key in ITEMS_DICT.keys():
        tmp_list.append(ITEMS_DICT[key])
    return tmp_list


@app.put("/item/{item_id}",
         summary="updates an item by id",
         tags=["Items"],
         response_model=Item)
def update_item(item: ItemIn):
    """
    Update **name**, **country_of_origin**, **count**,
    **weight**  with passed values. Use current id of an item as **id**.
    """
    id_validation(item.id)

    ITEMS_DICT[item.id].name = item.name
    ITEMS_DICT[item.id].country_of_origin = item.country_of_origin
    ITEMS_DICT[item.id].weight = item.weight
    ITEMS_DICT[item.id].count = item.count
    ITEMS_DICT[item.id].last_change_at = datetime.now()

    return ITEMS_DICT[item.id]


@app.delete("/item/{item_id}",
            summary="deletes an item by id",
            tags=["Items"])
def get_item(input_id: str):
    id_validation(input_id)
    del ITEMS_DICT[input_id]
    return {"message": f"Item with id = {input_id} deleted."}
