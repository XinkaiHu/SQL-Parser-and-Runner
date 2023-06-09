import os
import pandas as pd

from sql_runner import SQLRunner
from select import select


def insert_into(
    sql_runner: SQLRunner, table_name: str, attributes: list[str], values: list
):
    selected = select(
        sql_runner=sql_runner,
        table_name="__META",
        attributes=["PRIMARY_KEY"],
        conditions=("TABLE_NAME", lambda x: x == table_name),
    )
    if selected.empty:
        raise ValueError("No table named {}".format(table_name))
    primary_key = selected["PRIMARY_KEY"].values[0]
    if primary_key not in attributes:
        raise ValueError("Cannot insert without primary key {}.".format(primary_key))
    primary_key_value = values[attributes.index(primary_key)]
    if not select(
        sql_runner=sql_runner,
        table_name=table_name,
        attributes=[primary_key],
        conditions=(primary_key, lambda x: x == primary_key_value),
    ).empty:
        raise ValueError("Primary key {} existed.".format(primary_key_value))
    inserted = dict()
    for attribute, value in zip(attributes, values):
        inserted[attribute] = value
    df = pd.DataFrame(data=inserted, columns=attributes, index=[primary_key_value])

    path = os.path.join(sql_runner.database, table_name + ".csv")
    old = pd.read_csv(filepath_or_buffer=path, index_col=0)
    new = pd.concat(objs=[old, df])
    new.to_csv(path_or_buf=path)
