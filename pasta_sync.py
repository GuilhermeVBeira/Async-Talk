from time import sleep
import time
from time_it import timeit


def cook_pasta(i):
    print(f"Cooking pasta {i}")
    sleep(15)
    print(f"Pasta {i} is done {i}")

def fetch_pasta(i):
    print(f"Fetching the pasta {i} to cook")
    sleep(3)


def prepare_pasta(i):
    fetch_pasta(i)
    cook_pasta(i)


def main():
    for i in range(1, 3):
        prepare_pasta(i)

with timeit():
    main()
