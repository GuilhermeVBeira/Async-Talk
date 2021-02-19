import asyncio
import asyncpg
import string
import random
import time
import uvloop
from time_it import timeit



def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(string_length))


async def insert_many(conn):
    tasks = [(i, random_string()) for i in range(1000000)]
    return await conn.copy_records_to_table("role", records=tasks)

async def amain():

    conn = await asyncpg.connect(
        "postgresql://async_test:async_test@localhost/async_test"
    )
    await insert_many(conn)
    await conn.close()
uvloop.install()
with timeit():
    asyncio.run(amain())

