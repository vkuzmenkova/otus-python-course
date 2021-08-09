from functools import wraps
from pprint import pprint

from sqlalchemy.orm import joinedload

from models import User, Author, Article
from models.database import Base, Session
from faker import Faker


def create_tables():
    Base.metadata.create_all()


def create_many_users():
    user = User()


def get_authors():
    session = Session()
    author = session.query(Author).first()
    print(author)
    print(author.user)

    session.close()


def try_joinload():
    session = Session()
    query = session.query(User).options(joinedload(User.author))
    for user in query.all():
        print(user)
        print(user.author)
    session.close()


def load_articles():
    session = Session()
    query = session.query(User).options(joinedload(User.author).joinedload(Author.articles))
    all_stuff = query.all()
    for user in all_stuff:
        print("user:", user)
        print("user's author", user.author)
        for article in user.author.articles:
            print("author's article", article)
        print("=============================")


    session.close()


def main():
    # create_tables()
    # get_authors()
    # try_joinload()
    load_articles()


if __name__ == '__main__':
    main()
