from sqlalchemy import create_engine, MetaData, Table, Column, Integer, \
    String, Boolean

engine = create_engine("sqlite:///example-db-01.sqlite", echo=True)
metadata = MetaData()

items_db = Table(
    "items",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(100), unique=True),
    Column("is_staff", Boolean, nullable=False, default=False)
)


def main():
    metadata.create_all(engine)


if __name__ == "__main__":
    main()
