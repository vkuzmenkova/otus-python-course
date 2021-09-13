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
    func, ForeignKey, Text
)
from sqlalchemy.orm import relationship

from .db import Base, Session
from .mixins import TimestampMixin


class Author(TimestampMixin, Base):
    nickname = Column(String(32), nullable=False)
    user_id = Column(Integer, ForeignKey("blog_users.id"), nullable=False, unique=True)
    bio = Column(Text, default="Hey, I'm using App!", server_default="Hey, I'm using App!")

    user = relationship("User", back_populates="author")
    articles = relationship("Article", back_populates="author")

    def __str__(self):
        return f"ID:{self.id}, nickname: {self.nickname}"



