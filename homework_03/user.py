from dataclasses import dataclass
from pydantic import BaseModel
import datetime


@dataclass
class User():
    id: str
    name: str

