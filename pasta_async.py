import asyncio
import time
from time_it import timeit


async def cook_pasta(number):
    print(f"Preparing pasta {number}")
    await asyncio.sleep(15)
    print(f"Pasta {number} is done")


async def fetch_pasta(number):
    await asyncio.sleep(3)
    print(f"Fetching pasta {number} to cook")


async def main():
    tasks = []
    for i in range(1, 3):
        await fetch_pasta(i)
        task = asyncio.create_task(cook_pasta(i), name=f"Cooking pasta {i}")
        tasks.append(task)
    await asyncio.gather(*tasks)


with timeit():
    asyncio.run(main())
