from dataclasses import dataclass
from pydantic import BaseModel, Field
from datetime import datetime
import uuid

# пишем в csv: загружаем при каждом запуске и выгружаем при окончании
# работы программы
ITEMS_DICT = {}


class ItemBase(BaseModel):
    name: str
    country_of_origin: str
    entity: int
    weight: float


class ItemIn(ItemBase):
    id: str


class Item(ItemIn):
    created_at: datetime
    last_change_at: datetime
