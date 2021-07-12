from pydantic import BaseModel, Field, validator
from datetime import datetime

# пишем в csv: загружаем при каждом запуске и выгружаем при окончании
# работы программы
ITEMS_DICT = {}


class ItemBase(BaseModel):
    name: str
    country_of_origin: str
    entity: int
    weight: float

    """
    Как проверить, что приходит именно integer? Сейчас float автоматически 
    приводится
    """

    # @validator('entity')
    # def is_integer(cls, value):
    #     assert isinstance(value, int), ValueError("Value must be integer.")
    #     return value

    @validator('entity', 'weight')
    def is_positive(cls, value):
        assert value >= 0, ValueError("Value must be >= 0.")
        return value


"""
Переопределить порядок следования полей (id выводится слишком низко)/ 
по-другому задизайнить классы (иначе приходится повторять код и 
переопределять валидаторы)

"""


class ItemIn(ItemBase):
    id: str


# class ItemIn(BaseModel):
#     id: str
#     name: str
#     country_of_origin: str
#     entity: int
#     weight: float


class Item(ItemIn):
    created_at: datetime = Field(default_factory=datetime.now)
    last_change_at: datetime
