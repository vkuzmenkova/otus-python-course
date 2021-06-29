from pydantic import BaseModel, Field, ValidationError, validator, \
    root_validator


# https://pydantic-docs.helpmanual.io/usage/validators/#reuse-validators

class Tag(BaseModel):
    id: int
    tag_name: str


class User(BaseModel):
    id: int
    username: str = Field(alias='userFullName')
    friends: list[int]
    tags: list[Tag]
    password1: str
    password2: str

    @validator('username')
    def is_name_long_enough(cls, name: str):
        assert len(name) >= 10, ValueError('Name\'s length should be longer '
                                           'than 10.')
        return name

    @validator('friends', pre=True, each_item=True)
    def is_item_greater_than_ten(cls, item: int):
        assert item >= 10, ValueError('Item in List should be greater '
                                      'than 10.')
        return item

    @root_validator
    def check_password(cls, values):
        pw1 = values.get('password1')
        pw2 = values.get('password2')
        assert pw1 == pw2, ValueError('Passwords do not match.')
        return values


in_json: str = """{
        "id": 2.7, 
        "userFullName": "John Smith",
        "friends": [34, 56, 67],
        "tags": [
            {
                "id": 2,
                "tag_name": "banned"  
            },
            {
                "id": 3,
                "tag_name": "offline"  
            }
        ],
        "password1": "1234",
        "password2": "1234"
    }
    """

try:
    user = User.parse_raw(in_json)
except ValidationError as ex:
    print(ex.json())

print(user)
print(user.json(by_alias=True, exclude={"password1", "password2"}))
