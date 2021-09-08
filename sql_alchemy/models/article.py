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
    func, Text, ForeignKey
)
from sqlalchemy.orm import relationship

from .db import Base, Session
from .mixins import TimestampMixin


class Article(TimestampMixin, Base):
    title = Column(String(100), nullable=False, default="No name", server_default="Noname")
    body = Column(Text, nullable="", default="draft text", server_default="Draft text")
    status = Column(String(10), nullable=False, default="text", server_default="Draft")

    author_id = Column(Integer, ForeignKey("blog_authors.id"), nullable=False)
    author = relationship("Author", back_populates="articles")

    def __str__(self):
        return f"ID:{self.id} {self.title}"
