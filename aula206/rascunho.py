# PyMySQL - um cliente MySQL feito em python puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# GitHub: https://github.com/PyMySQL/PyMySQL
# type:ignore

import os

import pymysql
import pymysql.cursors
import sql

from dotenv import load_dotenv

load_dotenv()

connection = pymysql.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

with connection:
    # Verifica se a tabela já existe
    with connection.cursor() as cursor:
        cursor.execute(sql.CREATE_TABLE_CUSTOMERS)
    connection.commit()

    # Insere dados na tabela
    # continua a partir do último ponto
    with connection.cursor() as cursor:
        result_insert = cursor.executemany(
            sql.INSERT_INTO_CUSTOMERS,
            [
                ["Lucas", 25],
                ["Ana", 30],
                ["João", 35],
                ["Maria", 28],
                ["Pedro", 40],
                ["Carla", 22],
                ["Fernanda", 29],
                ["Roberto", 33],
                ["Juliana", 27],
                ["Ricardo", 31],
                ["Patrícia", 26],
                ["Eduardo", 34],
            ],
        )
        print(f"{result_insert} registros inseridos com sucesso!")
        cursor.execute(sql.TRUNCATE_CUSTOMERS)

    # Limpa a tabela antes de inserir novos dados
    # cursor.execute(sql.TRUNCATE_CUSTOMERS)

    # cursor.execute(sql.TRUNCATE_CUSTOMERS) #comando aqui
    connection.commit()
    with connection.cursor() as cursor:
        cursor.executemany(
            sql.INSERT_INTO_CUSTOMERS_DICT,
            [
                {
                    "name": "Lucas",
                    "age": 25,
                },
                {
                    "name": "Ana",
                    "age": 30,
                },
                {
                    "name": "João",
                    "age": 35,
                },
                {
                    "name": "Maria",
                    "age": 28,
                },
                {
                    "name": "Pedro",
                    "age": 40,
                },
                {
                    "name": "Carla",
                    "age": 22,
                },
                {
                    "name": "Fernanda",
                    "age": 29,
                },
            ],
        )
    connection.commit()

    with connection.cursor() as cursor:
        cursor.execute(sql.SELECT_CUSTOMERS)

        for row in cursor.fetchall():
            print(row)

    # with connection.cursor() as cursor:
    # cursor.execute(sql.DELETE_ONE_CUSTOMERS, (,))

    # with connection.cursor() as cursor:
    #     cursor.execute(sql.DELETE_ALL_CUSTOMERS)
    # connection.commit()

# cursor = connection.cursor()
# cursor.close()
# connection.close()
