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
from .articles_tags import articles_tags_table


class Article(TimestampMixin, Base):
    title = Column(String(100), nullable=False, default="No name", server_default="Noname")
    body = Column(Text, nullable=True, default="draft text",
                  server_default='Draft text')
    status = Column(String, default="text", server_default='Draft',
                    nullable=True)

    author_id = Column(Integer, ForeignKey("blog_authors.id"), nullable=False)
    author = relationship("Author", back_populates="articles")
    tags = relationship("Tag",
                        secondary=articles_tags_table,
                        back_populates="articles")

    def __str__(self):
        return f"ID:{self.id} {self.title}"
