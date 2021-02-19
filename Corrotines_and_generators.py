import asyncio


def some_generator():
    yield 1
    to_return = yield 2
    yield to_rejturn
    yield 3
    yield 4


@asyncio.coroutine
def old_coroutine():
    yield from some_generator()
    yield from some_generator()



class Awaitable:
    def __await__(self):
        return some_generator()

async def new_coroutine():
    await Awaitable()
        


# try:
#     coroutine.send(None)
# except StopIteration as e:
#     print(e.value)
