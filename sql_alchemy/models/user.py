from datetime import datetime

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    create_engine,
    func
)
from sqlalchemy.orm import relationship

from .db import Base, Session
from .mixins import TimestampMixin


class User(TimestampMixin, Base):
    username = Column(String(100), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)
    birth_date = Column(String, nullable=False)

    author = relationship("Author", back_populates="user", uselist=False)

    def __str__(self):
        return f"ID:{self.id} {self.username}, born {self.birth_date}"
