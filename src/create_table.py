import os
import pandas as pd

from sql_runner import SQLRunner
from select import select
from insert_into import insert_into


def create_table(
    sql_runner: SQLRunner, table_name: str, attributes: list[str], primary_key: str
) -> None:
    if primary_key not in attributes:
        raise ValueError("No attribute named {}.".format(primary_key))
    if not select(
        sql_runner=sql_runner,
        table_name="__META",
        attributes=["TABLE_NAME"],
        conditions=("TABLE_NAME", lambda x: x == table_name),
    ).empty:
        raise ValueError("Table {} existed.".format(table_name))
    insert_into(
        sql_runner=sql_runner,
        table_name="__META",
        attributes=["TABLE_NAME", "ATTRIBUTES", "PRIMARY_KEY"],
        values=[table_name, ",".join(attributes), primary_key],
    )

    path = os.path.join(sql_runner.database, table_name + ".csv")
    df = pd.DataFrame(columns=attributes)
    df.to_csv(path_or_buf=path)
