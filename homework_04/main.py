"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from typing import List

from aiohttp import ClientSession

from jsonplaceholder_requests import USERS_DATA_URL, POSTS_DATA_URL, fetch_json, \
    fetch_users_data, fetch_posts_data

from models import User, Post, Base, async_session, engine


async def async_main():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    #
    # users_data: List[dict]
    # posts_data: List[dict]
    # users_data, posts_data = await asyncio.gather(
    #     fetch_users_data(),
    #     fetch_posts_data(),
    # )
    #
    # users: List[User]
    # posts: List[Post]
    #
    # with async_session as session:
    #     async with session.begin():
    #         session.add_all(users)

    await engine.dispose()


def main():

    asyncio.run(async_main())


if __name__ == "__main__":
    main()
