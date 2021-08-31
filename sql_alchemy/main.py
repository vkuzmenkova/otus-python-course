from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    create_engine
)
from sqlalchemy.orm import declarative_base

# collection, describes all the tables
metadata = MetaData()
engine = create_engine("sqlite:///example-db-01.sqlite", echo=True)

# Construct a base class for declarative class definitions.
# The new base class will be given a metaclass that produces appropriate Table objects and makes the appropriate mapper()
# calls based on the information provided declaratively in the class and any subclasses of the class.
Base = declarative_base(bind=engine)  # bind – An optional Connectable, will be assigned the bind attribute on the MetaData instance.


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True),
    name = Column(String(100)),
    surname = Column(String)


if __name__ == '__main__':
    for table in metadata.sorted_tables:
        print(table.name)

    Base.metadata.create_all()
