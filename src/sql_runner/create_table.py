def create_table(
    database_name: str, table_name: str, attributes: list[str], primary_key: str
):
    import os
    import pandas as pd

    from sql_runner.my_select import my_select
    from sql_runner.insert_into import insert_into

    if primary_key not in attributes:
        raise ValueError("No attribute named {}.".format(primary_key))
    if not my_select(
        database_name=database_name,
        table_name="__META",
        attributes=["TABLE_NAME"],
        conditions=("TABLE_NAME", lambda x: x == table_name),
    ).empty:
        raise ValueError("Table {} existed.".format(table_name))
    insert_into(
        database_name=database_name,
        table_name="__META",
        attributes=["TABLE_NAME", "ATTRIBUTES", "PRIMARY_KEY"],
        values=[table_name, ",".join(attributes), primary_key],
    )

    path = os.path.join(database_name, table_name + ".csv")
    df = pd.DataFrame(columns=attributes)
    df.to_csv(path_or_buf=path)
    return df
