from dataclasses import dataclass
from pydantic import BaseModel, Field
from datetime import datetime
import uuid

# пишем в csv: загружаем при каждом запуске и выгружаем при окончании
# работы программы
ITEMS_DICT = {}


class ItemIn(BaseModel):
    name: str
    country_of_origin: str
    entity: int
    weight: float


class Item(ItemIn):
    id: str
