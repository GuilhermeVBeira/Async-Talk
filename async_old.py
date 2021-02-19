import asyncio
import time
from time_it import timeit

loop = asyncio.get_event_loop()


async def cook_pasta(number):
    print(f"Cooking pasta {number}")
    await asyncio.sleep(15)
    print(f"Pasta {number} is done {number}")


async def fetch_pasta(number):
    await asyncio.sleep(3)
    print(f"Fetching the pasta {number} to cook")


async def check_tasks(tasks):
    while True:
        if all(task.done() for task in tasks):
            print("All tasks are finished")
            loop.stop()
        await asyncio.sleep(0.1)


async def main():
    tasks = []
    for i in range(1, 3):
        await fetch_pasta(i)
        task = loop.create_task(cook_pasta(i))
        tasks.append(task)
    await check_tasks(tasks)




with timeit():
    loop.create_task(main())
    loop.run_forever()


