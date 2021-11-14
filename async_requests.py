"""
This file is just a test script for experimenting with async
http requests. It is not a main part of this small project
"""

import asyncio
import aiohttp
import async_timeout
import time


async def fetch_page(url, session):
    page_start = time.time()
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            print(f"Page took {time.time() - page_start}")
            return response.status


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(url, session))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


loop = asyncio.get_event_loop()

urls = ["http://google.com" for i in range(50)]
start = time.time()
loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f"All took {time.time() - start}")
