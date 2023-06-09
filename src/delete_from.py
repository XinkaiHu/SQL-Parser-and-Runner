import os
import pandas as pd

from sql_runner import SQLRunner
from select import select


def delete_from(
    sql_runner: SQLRunner, table_name: str, conditions: tuple | None = None
) -> None:
    source_table = select(
        sql_runner=sql_runner,
        table_name="__META",
        attributes=["ATTRIBUTES", "PRIMARY_KEY"],
        conditions=("TABLE_NAME", lambda x: x == table_name),
    )

    if source_table.empty:
        raise ValueError("No table named {}".format(table_name))
    attributes = source_table["ATTRIBUTES"].values[0].split(",")
    deleted = select(
        sql_runner=sql_runner,
        table_name=table_name,
        attributes=attributes,
        conditions=conditions,
    )

    path = os.path.join(sql_runner.database, table_name + ".csv")
    old = pd.read_csv(filepath_or_buffer=path, index_col=0)
    new = old.drop(deleted.index.values)
    new.to_csv(path_or_buf=path)
