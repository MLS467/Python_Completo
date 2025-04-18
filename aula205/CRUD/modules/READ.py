from modules.connection import DB_TABLE_NAME, con, con_start


@con
def read_data(cursor=None) -> None:
    con_start()
    sql = f"""
    SELECT * FROM {DB_TABLE_NAME}
    """
    result = cursor.execute(sql)  # type: ignore

    for row in result:
        print(row)


if __name__ == "__main__":
    read_data()
