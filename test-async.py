from time import sleep
from loguru import logger
import asyncio


def sync_foo():
    logger.info("sync_foo start")
    sleep(3)
    logger.info("sync_foo finish")


def sync_bar():
    logger.info("sync_bar start")
    sleep(3)
    logger.info("sync_bar finish")


async def async_foo():
    logger.info("async_foo start")
    await asyncio.sleep(4)
    logger.info("async_foo finish")


async def async_bar():
    logger.info("async_bar start")
    await asyncio.sleep(3)
    logger.info("async_bar finish")


async def run_my_async():
    await async_foo()
    await async_bar()


async def run_main():
    logger.info("run_main async start")
    coros = {
        async_foo(),
        async_bar(),
    }
    logger.info("coros created, awaiting ...")
    await asyncio.wait([asyncio.create_task(coro) for coro in coros])
    logger.info("run_main async finish")


async def do_smth_async(num: int):
    logger.info("do_smth_async {} async start", num)
    if num % 3 == 0:
        await asyncio.sleep(1.5)
    else:
        await asyncio.sleep(1)
    logger.info("do_smth_async {} async finish", num)


async def run_many_async_func(count: int):
    logger.info("run_many_async_func async start")
    coros = {
        do_smth_async(i) for i in range(count)
    }
    logger.info("{} coros created, awaiting ...", count)
    await asyncio.wait([asyncio.create_task(coro) for coro in coros])
    logger.info("run_many_async_func async finish")

def main():
    logger.info("main start")
    asyncio.run(run_many_async_func(12))
    logger.info("main finish")


if __name__ == '__main__':
    main()
