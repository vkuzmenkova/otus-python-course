from pydantic import BaseModel, Field, validator
from datetime import datetime

ITEMS_DICT = {}


class ItemBase(BaseModel):
    name: str
    country_of_origin: str
    entity: int
    weight: float

    @validator('entity', 'weight')
    def is_positive(cls, value):
        assert value >= 0, ValueError("Value must be >= 0.")
        return value

    # Проверить, что в entity приходит целое
    # @validator('entity')
    # def is_number_integer(cls, value):
    #     assert str(value).isdigit(), ValueError("Value must be integer.")
    #     return value


class ItemIn(ItemBase):
    id: str


class Item(ItemIn):
    created_at: datetime = Field(default_factory=datetime.now)
    last_change_at: datetime
