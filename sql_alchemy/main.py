from faker import Faker
from faker.generator import random
from sqlalchemy.orm import joinedload

from models.db import Base, Session
from models.user import User
from models.author import Author
from sql_alchemy.models import Article
from sql_alchemy.models import Tag

NUMBER_OF_USERS = 1000
NUMBER_OF_AUTHORS = 30


def create_items(items_list):
    session = Session()

    for item in items_list:
        session.add(item)

    session.commit()
    session.close()


def get_item_by_id(item_id, cls):
    with Session() as session:
        item: cls = session.query(cls).get(item_id)

        if cls == Author:
            print(item.user)
        if cls == User:
            print(item.author)

    return item


def generate_users_for_db():
    user_list = []
    fake = Faker()

    for i in range(NUMBER_OF_USERS):
        user = User(username=str(fake.unique.name()).lower().replace(' ', '_').replace('.', '_'),
                    is_staff=random.randint(0, 1),
                    birth_date=fake.date())
        user_list.append(user)

    create_items(user_list)


def generate_authors_for_db():
    authors_list = []

    for i in range(NUMBER_OF_AUTHORS):
        user: User = get_item_by_id(random.randint(0, NUMBER_OF_USERS), User)
        username_parts = user.username.capitalize().split('_')
        author = Author(nickname=username_parts[0] + ' ' + username_parts[1][:1].capitalize() + '.', user_id=user.id)
        authors_list.append(author)

    create_items(authors_list)


def get_authors_with_users():
    with Session() as session:
        authors_with_users = session.query(Author).all()
        for author in authors_with_users:
            print(f"AUTHOR: {author} CONNECTED WITH USER: {author.user}")


def get_users_with_authors():
    with Session() as session:
        users_with_authors = session.query(User).all()
        for user in users_with_authors:
            print(f"USER: {user} CONNECTED WITH AUTHOR: {user.author}")


def get_all_articles():
    with Session() as session:
        articles = session.query(Article).all()
        for article in articles:
            print(f"ARTICLE: {article} CREATED BY {article.author} CONNECTED WITH USER: {article.author.user}")


def get_all_users_with_articles():
    with Session() as session:
        users = session.query(User).options(joinedload(User.author).joinedload(Author.articles))

        for user in users:
            if user.author is not None and user.author.articles != []:
                print(user)


def get_all_users_with_python_articles():
    with Session() as session:
        users = session.query(User).join(Author, Author.user_id == User.id).join(Article, Article.author_id == Author.id).filter(Article.title.ilike("%Python%")).all()

        for user in users:
            print(user)


def get_all_tags():
    with Session() as session:
        tag = session.query(Tag).filter(Tag.name.ilike("%python%")).one_or_none()
        python_articles = session.query(Article).filter(Article.title.ilike("%python%"))

        for article in python_articles:
            article.tags.append(tag)

        session.commit()


if __name__ == '__main__':
    # Base.metadata.create_all()
    # generate_users_for_db()
    # generate_authors_for_db()

    # author_id = random.randint(1, NUMBER_OF_AUTHORS)
    # author_ex = get_item_by_id(author_id, Author)
    # user_ex = get_item_by_id(get_item_by_id(author_id, Author).user_id, User)
    # print(f"USER: {user_ex} IS AUTHOR: {author_ex}")

    # get_authors_with_users()
    # get_users_with_authors()
    # get_all_articles()
    # get_all_users_with_articles()
    # get_all_users_with_python_articles()
    get_all_tags()
