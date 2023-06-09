import os
import pandas as pd

from sql_runner import SQLRunner


def init_meta(sql_runner: SQLRunner) -> None:
    meta = {
        "TABLE_NAME": "__META",
        "ATTRIBUTES": ",".join(["TABLE_NAME", "ATTRIBUTES", "PRIMARY_KEY"]),
        "PRIMARY_KEY": "TABLE_NAME",
    }
    df = pd.DataFrame(data=meta, index=["__META"])

    meta_path = os.path.join(sql_runner.database, "__META.csv")
    df.to_csv(path_or_buf=meta_path)
