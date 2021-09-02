from faker.generator import random
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    create_engine,
    func
)
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from datetime import datetime
from faker import Faker

# metadata = MetaData()
engine = create_engine("sqlite:///db1.sqlite", echo=False)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


# users_table = Table(
#     "users",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("username", String(100), unique=True),
#     Column("is_staff", Boolean, nullable=False, default=False)
# )


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    is_staff = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow,
                        server_default=func.now())
    birth_date = Column(String, nullable=False)

    def __str__(self):
        return f"ID:{self.id} {self.username}, born {self.birth_date}"


def create_users(user_list):
    session = Session()

    for user in user_list:
        session.add(user)

    session.commit()

    session.close()


def get_user_by_id(user_id):
    with Session() as session:
        user: User = session.query(User).filter_by(id=user_id).one()

    return user


if __name__ == '__main__':
    Base.metadata.create_all()

    user_list = []
    fake = Faker()

    # for i in range(1000):
    #     user = User(username=fake.unique.name(), is_staff=True,
    #                 birth_date=fake.date())
    #     user_list.append(user)
    #
    # create_users(user_list)

    print(str(get_user_by_id(193)))
    print(str(get_user_by_id(711)))
    print(str(get_user_by_id(343)))
