from pydantic import BaseModel, Field, validator
from datetime import datetime


class ItemBase(BaseModel):
    """
    input schema for GET /items/create
    """
    name: str
    country_of_origin: str
    count: int
    weight: float

    @validator('count')
    def is_count_valid(cls, value):
        assert str(value).isdigit(), ValueError("Value must be integer.")
        assert value >= 0, ValueError("Value must be >= 0.")
        return value

    @validator('weight')
    def is_weight_valid(cls, value):
        assert value > 0, ValueError("Value must be > 0.")
        return value


class ItemIn(ItemBase):
    """
    schema for PUT /items/{item_id}/update
    """
    id: str


class Item(ItemIn):
    """
    schema for keeping an item in store
    """
    created_at: datetime = Field(default_factory=datetime.now)
    last_change_at: datetime
