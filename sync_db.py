import psycopg2
import string
import random
from time_it import timeit

SQL_INSERT = (
    """ INSERT INTO role (role_id, role_name) VALUES (%(role_id)s, %(role_name)s);"""
)


def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(string_length))


conn = psycopg2.connect(
    dbname="async_test", user="async_test", password="async_test", host="127.0.0.1"
)


def main():
    cur = conn.cursor()
    tasks = [({"role_id": i, "role_name": random_string()}) for i in range(1000000)]
    cur.executemany(SQL_INSERT, tuple(tasks))
    conn.commit()
    cur.close()
    conn.close()

with timeit():
    main()

