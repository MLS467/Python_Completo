# type:ignore
from sqlite3 import Cursor

from modules.connection import DB_TABLE_NAME, con


@con
def update_row(id_: int, data: list = [], cursor: Cursor = None) -> None:
    name, age, height = data
    sql = f"""
        UPDATE {DB_TABLE_NAME}
        SET name=:name, age={age}, height = {height}
        WHERE id=:id
    """

    if cursor.execute(
        sql, {"name": name, "age": age, "height": height, "id": id_}
    ):
        print("Atualizado com sucesso!")
        return

    print("Erro ao atualizar")


if __name__ == "__main__":
    data = ["JOÃOZÃO", 60, 1.65]
    update_row(9, data=data)
