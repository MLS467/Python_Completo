TABLE_NAME = "customers"

CREATE_TABLE_CUSTOMERS = f"""

            CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT
            );

            """

INSERT_INTO_CUSTOMERS = f"""
    INSERT INTO {TABLE_NAME}
    (name, age)
    VALUES
    (%s, %s)
"""

INSERT_INTO_CUSTOMERS_DICT = f"""
    INSERT INTO {TABLE_NAME}
    (name, age)
    VALUES
    (%(name)s, %(age)s)
"""

TRUNCATE_CUSTOMERS = f"""
    TRUNCATE TABLE {TABLE_NAME};
"""

SELECT_CUSTOMERS = f"""
    SELECT * FROM {TABLE_NAME};
"""

DELETE_ALL_CUSTOMERS = f"""
DELETE FROM {TABLE_NAME}
"""

DELETE_ONE_CUSTOMERS = f"""
DELETE FROM {TABLE_NAME} WHERE id = %s
"""

UPDATE_DATA_CUSTOMERS = f"""
UPDATE {TABLE_NAME} SET name = %s
WHERE id = %s
"""
