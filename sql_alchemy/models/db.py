from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, declared_attr


class Base:

    @declared_attr
    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow,
                        server_default=func.now())


engine = create_engine("sqlite:///db.sqlite", echo=False)
Base = declarative_base(cls=Base, bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


