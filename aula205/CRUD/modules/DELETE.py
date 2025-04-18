# type:ignore
from sqlite3 import Cursor

from modules.connection import DB_TABLE_NAME, con


@con
def delete_row(id_: int, cursor: Cursor = None) -> None:
    sql = f"""
    DELETE FROM {DB_TABLE_NAME} WHERE id=:id
    """
    if cursor.execute(sql, {"id": id_}):
        print("Deletado com sucesso!")
        return

    print("Erro ao deletar!")


if __name__ == "__main__":
    delete_row(8)
