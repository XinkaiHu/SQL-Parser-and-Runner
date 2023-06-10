def delete_from(
    database_name: str, table_name: str, conditions: tuple | None = None
):
    import os
    import pandas as pd

    from sql_runner.my_select import my_select

    source_table = my_select(
        database_name=database_name,
        table_name="__META",
        attributes=["ATTRIBUTES", "PRIMARY_KEY"],
        conditions=("TABLE_NAME", lambda x: x == table_name),
    )

    if source_table.empty:
        raise ValueError("No table named {}".format(table_name))
    attributes = source_table["ATTRIBUTES"].values[0].split(",")
    deleted = my_select(
        database_name=database_name,
        table_name=table_name,
        attributes=attributes,
        conditions=conditions,
    )

    path = os.path.join(database_name, table_name + ".csv")
    old = pd.read_csv(filepath_or_buffer=path, index_col=0)
    new = old.drop(deleted.index.values)
    new.to_csv(path_or_buf=path)
    return new
