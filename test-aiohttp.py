import asyncio
from asyncio import FIRST_COMPLETED
from dataclasses import dataclass
from loguru import logger
from aiohttp import ClientSession


@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service("ip-api", "http://ip-api.com/json", "query"),
    Service("ipify", "https://api.ipify.org/?format=json", "ip")
]


async def fetch_json(session: ClientSession, url):
    async with session.get(url) as response:
        return await response.json()


async def fetch_ip(service: Service) -> str:
    logger.info("fetch ip from {}", service.name)
    async with ClientSession() as session:
        result = await fetch_json(session, service.url)
    logger.info("fetched json from {}: {}", service.name, result)

    return result.get(service.field)


async def get_my_ip(timeout):
    tasks = {
        asyncio.create_task(fetch_ip(service))
        for service in SERVICES
    }
    coro = asyncio.wait(tasks, timeout=timeout, return_when=FIRST_COMPLETED)
    done, pending = await coro
    for p_task in pending:
        p_task.cancel()
        logger.info("cancelled  task {}", p_task)

    ip = ""
    for task in done:
        task.result()
        break
    else:
        logger.warning("cant fetch ip")
    return ip


asyncio.run(get_my_ip(0.5))
