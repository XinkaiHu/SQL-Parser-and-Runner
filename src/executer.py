import os

import pandas as pd


class SQLRunner:
    def __init__(self, database_name: str) -> None:
        if not os.path.exists(database_name):
            os.mkdir(path=database_name)
        self.database = database_name

        meta = dict()
        meta["TABLE_NAME"] = ("__META",)
        meta["ATTRIBUTES"] = ("TABLE_NAME,ATTRIBUTES,PRIMARY_KEY",)
        meta["PRIMARY_KEY"] = ("TABLE_NAME",)
        df = pd.DataFrame(data=meta, index=["__META"])

        meta_path = os.path.join(database_name, "__META.csv")
        df.to_csv(path_or_buf=meta_path)

    def create_table(
        self, table_name: str, attributes: list[str], primary_key: str
    ) -> None:
        if primary_key not in attributes:
            raise ValueError("No attribute named {}.".format(primary_key))
        if not self.select(
            table_name="__META",
            attributes=["TABLE_NAME"],
            conditions=("TABLE_NAME", lambda x: x == table_name),
        ).empty:
            raise ValueError("Table {} existed.".format(table_name))
        self.insert_into(
            table_name="__META",
            attributes=["TABLE_NAME", "ATTRIBUTES", "PRIMARY_KEY"],
            values=[table_name, ",".join(attributes), primary_key],
        )

        path = os.path.join(self.database, table_name + ".csv")
        df = pd.DataFrame(columns=attributes)
        df.to_csv(path_or_buf=path)

    def drop_table(self, table_name: str):
        if table_name == "__META":
            raise ValueError("Cannot delete meta data.")
        path = os.path.join(self.database, table_name + ".csv")
        os.remove(path=path)
        self.delete_from(
            table_name="__META", conditions=("TABLE_NAME", lambda x: x == table_name)
        )

    def insert_into(self, table_name: str, attributes: list[str], values: list):
        selected = self.select(
            table_name="__META",
            attributes=["PRIMARY_KEY"],
            conditions=("TABLE_NAME", lambda x: x == table_name),
        )
        if selected.empty:
            raise ValueError("No table named {}".format(table_name))
        primary_key = selected["PRIMARY_KEY"].values[0]
        if primary_key not in attributes:
            raise ValueError(
                "Cannot insert without primary key {}.".format(primary_key)
            )
        primary_key_value = values[attributes.index(primary_key)]
        if not self.select(
            table_name=table_name,
            attributes=[primary_key],
            conditions=(primary_key, lambda x: x == primary_key_value),
        ).empty:
            raise ValueError("Primary key {} existed.".format(primary_key_value))
        inserted = dict()
        for attribute, value in zip(attributes, values):
            inserted[attribute] = value
        df = pd.DataFrame(data=inserted, columns=attributes, index=[primary_key_value])

        path = os.path.join(self.database, table_name + ".csv")
        old = pd.read_csv(filepath_or_buffer=path, index_col=0)
        new = pd.concat(objs=[old, df])
        new.to_csv(path_or_buf=path)

    def delete_from(self, table_name: str, conditions: tuple | None = None) -> None:
        source_table = self.select(
            table_name="__META",
            attributes=["ATTRIBUTES", "PRIMARY_KEY"],
            conditions=("TABLE_NAME", lambda x: x == table_name),
        )
        if source_table.empty:
            raise ValueError("No table named {}".format(table_name))
        attributes = source_table["ATTRIBUTES"].values[0].split(",")
        deleted = self.select(
            table_name=table_name, attributes=attributes, conditions=conditions
        )

        path = os.path.join(self.database, table_name + ".csv")
        old = pd.read_csv(filepath_or_buffer=path, index_col=0)
        new = old.drop(deleted.index.values)
        new.to_csv(path_or_buf=path)

    def select(
        self,
        table_name: str | list[str],
        attributes: list[str],
        conditions: tuple | None = None,
    ) -> pd.DataFrame:
        if isinstance(table_name, str):
            path = os.path.join(self.database, table_name + ".csv")
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


runner = SQLRunner("MyDatabase")
runner.create_table("MyTable", ["A", "B", "C"], "A")
runner.create_table("YourTable", ["E", "F", "G"], "E")
runner.insert_into("MyTable", ["A", "C"], [1, 3])
runner.insert_into("MyTable", ["A", "B"], [2, 4])
runner.insert_into("MyTable", ["A", "C", "B"], [-2, -4, -3])
runner.delete_from("MyTable", ("A", lambda x: x == 1))
runner.drop_table("YourTable")
