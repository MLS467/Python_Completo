# type:ignore

from dotenv import load_dotenv
import os
import pymysql
from aula206.sql import INSERT_INTO_CUSTOMERS_DICT, TRUNCATE_CUSTOMERS

load_dotenv()

con = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
    charset="utf8mb4",
)


data_simulator = [
    {"name": "Lucas", "age": 25},
    {"name": "Ana", "age": 30},
    {"name": "João", "age": 35},
    {"name": "Maria", "age": 28},
    {"name": "Pedro", "age": 40},
    {"name": "Carla", "age": 22},
    {"name": "Fernanda", "age": 29},
    {"name": "Roberto", "age": 33},
    {"name": "Juliana", "age": 27},
    {"name": "Ricardo", "age": 31},
    {"name": "Patrícia", "age": 26},
    {"name": "Eduardo", "age": 34},
    {"name": "Lucas", "age": 25},
    {"name": "Ana", "age": 30},
    {"name": "João", "age": 35},
    {"name": "Maria", "age": 28},
    {"name": "Pedro", "age": 40},
    {"name": "Carla", "age": 22},
    {"name": "Fernanda", "age": 29},
    {"name": "Roberto", "age": 33},
    {"name": "Juliana", "age": 27},
    {"name": "Ricardo", "age": 31},
    {"name": "Patrícia", "age": 26},
    {"name": "Eduardo", "age": 34},
]

with con:
    with con.cursor() as cursor:
        result = cursor.executemany(
            INSERT_INTO_CUSTOMERS_DICT,
            data_simulator,
        )
        print(f"{result} rows inserted")

        cursor.execute(TRUNCATE_CUSTOMERS)
    con.commit()
