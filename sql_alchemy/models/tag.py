from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import relationship

from .db import Base, Session
from .mixins import TimestampMixin
from .articles_tags import articles_tags_table


class Tag(TimestampMixin, Base):
    name = Column(String(20), unique=True, nullable=False)

    articles = relationship("Article",
                            secondary=articles_tags_table,
                            back_populates="tags")

    def __str__(self):
        return f"{self.name}"
