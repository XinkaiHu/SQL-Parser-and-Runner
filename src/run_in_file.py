from sql_parser.parser import parse_sql
from sql_runner.runner import run_sql
from sql_runner.create_database import create_database
from sql_runner.init_meta import init_meta

database_name = "MyDatabase"
create_database(database_name=database_name)
init_meta(database_name=database_name)
with open(file="test.sql", mode="r") as f:
    sqls = f.readlines()
    sqls = [sql + ";" for sql in "".join(sqls).split(";")[:-1]]
    for sql in sqls:
        type, args = parse_sql(sql=sql)
        print(type, args)
        df = run_sql(database_name=database_name, type=type, args=args)
        print(df)
