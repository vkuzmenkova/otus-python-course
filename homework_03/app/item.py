from pydantic import BaseModel, Field, validator, root_validator
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
    # @root_validator(pre=True)
    # As with field validators, root validators can have pre=True,
    # in which case they're called before field validation occurs
    # (and are provided with the raw input data)
    # - otherwise isinstance(value, int) doesn't work
    # api fails
    def is_count_valid(cls, value):
        # assert value >= 0, ValueError("Value must be >= 0.")
        # assert isinstance(value, int), ValueError("Value must be integer.")
        if value < 0:
            ValueError("Value must be >= 0.")
        if not isinstance(value, int):
            ValueError("Value must be integer.")

        return value

    @validator('weight')
    def is_weight_valid(cls, value):
        if value <= 0:
            ValueError("Value must be > 0.")
        # assert value > 0, ValueError("Value must be > 0.")
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
