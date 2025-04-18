from functools import wraps
import pathlib
import sqlite3

ROOT_FOLDER = pathlib.Path(__file__).parent.parent
DB_NAME = "exercicio.sqlite3"
DB_PATH = ROOT_FOLDER / DB_NAME
DB_TABLE_NAME = "users"


def con_start():
    sql = f"""
    CREATE TABLE IF NOT EXISTS {DB_TABLE_NAME}
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    age INTEGER,
    height REAL
    )
    """
    con(sql)


def con(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            connection = sqlite3.connect(DB_PATH)
            cursor = connection.cursor()

            result = func(cursor=cursor, *args, **kwargs)

            connection.commit()
            cursor.close()
            connection.close()
            return result
        except Exception as e:
            print(f"Erro na conexão: {e}")
            raise e

    return wrapper


if __name__ == "__main__":
    ...
