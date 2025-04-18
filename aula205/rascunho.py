import sqlite3
import pathlib

ROOT_FOLDER = pathlib.Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_PATH = ROOT_FOLDER / DB_NAME
NAME_TABLE = "Customer"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute(
    f"""
        CREATE TABLE IF NOT EXISTS {NAME_TABLE} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        weight REAL
    )
    """
)
# connection.commit()


sql = f"""
        INSERT INTO {NAME_TABLE}
        (name, age, weight)
        VALUES(:nome,:idade,:peso)
    """

# cursor.execute(sql
# ,[customer1["nome"], customer1["idade"], customer1["peso"]]
# )

cursor.executemany(
    sql,
    [
        {"nome": "Maisson", "idade": 29, "peso": 89.5},
        {"nome": "Luciane", "idade": 32, "peso": 89.5},
        {"nome": "Manuelle", "idade": 4, "peso": 20},
    ],
)

# cursor.execute(f"DELETE FROM {NAME_TABLE}")
connection.commit()

resposta = cursor.execute(f"""SELECT * FROM {NAME_TABLE}""")

cursor.close()
connection.close()
