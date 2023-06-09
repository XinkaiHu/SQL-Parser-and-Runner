import os
import pandas as pd

from sql_runner import SQLRunner


def select(
    sql_runner: SQLRunner,
    table_name: str | list[str],
    attributes: list[str],
    conditions: tuple | None = None,
) -> pd.DataFrame:
    if isinstance(table_name, str):
        path = os.path.join(sql_runner.database, table_name + ".csv")
        df = pd.read_csv(filepath_or_buffer=path, index_col=0)
        if conditions is not None:
            attribute, p = conditions
            selected = df.loc[p(df[attribute]), attributes]
        else:
            selected = df[attributes]
        print("================ SELECT ================")
        print(selected)
        return selected
    else:
        # 多表查询
        pass
