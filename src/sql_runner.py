import os


class SQLRunner:
    def __init__(self, database_name: str) -> None:
        if not os.path.exists(database_name):
            os.mkdir(path=database_name)
        self.database = database_name
