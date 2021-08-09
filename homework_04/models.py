"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, declared_attr, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


engine = create_engine(PG_CONN_URI, echo=True)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class User:
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    name = Column(String(32))
    email = Column(String(100))

    posts = relationship("Post", back_populates="user")


class Post:
    id = Column(Integer, primary_key=True)
    title = Column(String(100), default="No name")
    body = Column(String(10000), default="draft")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="posts")
