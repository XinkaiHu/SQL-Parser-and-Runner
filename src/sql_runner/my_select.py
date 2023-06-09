from sql_runner.merge_join import JoinMode


def my_select(
    database_name: str,
    table_name: str | list[str],
    attributes: list[str],
    conditions: tuple | None = None,
    mode: JoinMode = JoinMode.inner_join
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
        if conditions is not None:
            attribute, p = conditions
            if attribute in df:
                selected = df.loc[p(df[attribute]), attributes]
            else:
                selected = df[attributes]
        else:
            selected = df[attributes]
        return selected

    elif len(table_name) == 2:
        from sql_runner.merge_join import merge_join

        left_path = os.path.join(database_name, table_name[0] + ".csv")
        left_df = pd.read_csv(filepath_or_buffer=left_path, index_col=0)
        right_path = os.path.join(database_name, table_name[1] + ".csv")
        right_df = pd.read_csv(filepath_or_buffer=right_path, index_col=0)

        left_attributes = []
        right_attributes = []
        join_attributes = []
        if "*" in attributes:
            attributes = []
            for attribute in left_df:
                attributes.append(attribute)
            for attribute in right_df:
                attributes.append(attribute)
            attributes = list(set(attributes))

        for attribute in attributes:
            if attribute in left_df and attribute in right_df:
                join_attributes.append(attribute)
            if attribute in left_df:
                left_attributes.append(attribute)
            if attribute in right_df:
                right_attributes.append(attribute)

        left_df = my_select(database_name=database_name, table_name=table_name[0], attributes=left_attributes, conditions=conditions)
        right_df = my_select(database_name=database_name, table_name=table_name[1], attributes=right_attributes, conditions=conditions)
        df = merge_join(left=left_df, right=right_df, attributes=join_attributes, mode=mode)
        return df

    else:
        raise ValueError("Unsupported.")
