from functools import wraps
from pprint import pprint

from sqlalchemy.orm import joinedload

from models import User, Author, Article
from models.database import Base, Session


def create_tables():
    Base.metadata.create_all()


def main():
    create_tables()


if __name__ == '__main__':
    main()
