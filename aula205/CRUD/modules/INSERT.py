# type: ignore
from sqlite3 import Cursor
from modules.connection import DB_TABLE_NAME, con, con_start


@con
def insert_data(data: list = [], cursor: Cursor = None) -> None:
    con_start()
    sql = f"""
    INSERT INTO {DB_TABLE_NAME} 
    (name, age, height) 
    VALUES (?, ?, ?)
    """
    if len(data) == 1:
        cursor.execute(sql, *data)
    else:
        cursor.executemany(
            sql,
            ([(name, age, _height) for name, age, _height in data]),
        )


if __name__ == "__main__":
    data = [["Maisson", 29, 1.70], ["Luciane", 32, 1.65]]
    insert_data(data=data)
