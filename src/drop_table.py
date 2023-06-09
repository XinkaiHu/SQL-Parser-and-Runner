import os

from sql_runner import SQLRunner


def drop_table(sql_runner: SQLRunner, table_name: str):
    if table_name == "__META":
        raise ValueError("Cannot delete meta data.")
    path = os.path.join(sql_runner.database, table_name + ".csv")
    os.remove(path=path)
    sql_runner.delete_from(
        table_name="__META", conditions=("TABLE_NAME", lambda x: x == table_name)
    )
