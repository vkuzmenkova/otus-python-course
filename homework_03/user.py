from dataclasses import dataclass
from pydantic import BaseModel

from faker import Faker
import uuid

fake = Faker()

ERROR_USER_EXISTS = "User with this name already exists."




