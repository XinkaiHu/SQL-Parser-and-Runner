from sql_parser.parser import parse_sql
from sql_runner.runner import run_sql
from sql_runner.create_database import create_database
from sql_runner.init_meta import init_meta

database_name = input("Enter database name: ")
create_database(database_name=database_name)
init_meta(database_name=database_name)

while True:
    sql = input("Enter SQL: ")
    type, args = parse_sql(sql=sql)
    print(type, args)
    df = run_sql(database_name=database_name, type=type, args=args)
    print(df)
