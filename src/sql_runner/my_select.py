def my_select(
    database_name: str,
    table_name: str | list[str],
    attributes: list[str],
    conditions: tuple | None = None,
):
    import os
    import pandas as pd

    if len(table_name) == 1:
        table_name = table_name[0]
    if isinstance(table_name, str):
        path = os.path.join(database_name, table_name + ".csv")
        df = pd.read_csv(filepath_or_buffer=path, index_col=0)
        if "*" in attributes:
            attributes = df.columns.values
            print(attributes)
        if conditions is not None:
            attribute, p = conditions
            selected = df.loc[p(df[attribute]), attributes]
        else:
            selected = df[attributes]
        return selected
    else:
        return "TODO"
