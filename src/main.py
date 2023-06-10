# from sql_runner import SQLRunner
# from sql_runner.init_meta import init_meta
# from sql_runner.create_table import create_table
# from sql_runner.insert_into import insert_into
# from sql_runner.delete_from import delete_from
# from sql_runner.drop_table import drop_table
# from sql_runner.my_select import my_select
# from sql_runner.merge_join import merge_join, JoinMode


# sql_runner = SQLRunner(database_name="MyDatabase")

# init_meta(sql_runner=sql_runner)

# create_table(
#     sql_runner=sql_runner,
#     table_name="MyTable",
#     attributes=["Attr1", "Attr2", "Attr3"],
#     primary_key="Attr1",
# )

# create_table(
#     sql_runner=sql_runner,
#     table_name="YourTable",
#     attributes=["Attr1", "Attr4", "Attr5"],
#     primary_key="Attr1",
# )

# insert_into(
#     sql_runner=sql_runner,
#     table_name="MyTable",
#     attributes=["Attr1", "Attr2", "Attr3"],
#     values=[1, 2, 3],
# )

# insert_into(
#     sql_runner=sql_runner,
#     table_name="MyTable",
#     attributes=["Attr1", "Attr2"],
#     values=[2, 4],
# )

# insert_into(
#     sql_runner=sql_runner,
#     table_name="MyTable",
#     attributes=["Attr1", "Attr2", "Attr3"],
#     values=[3, 2, 4],
# )

# insert_into(
#     sql_runner=sql_runner,
#     table_name="YourTable",
#     attributes=["Attr1", "Attr4", "Attr5"],
#     values=[1, 2, 2],
# )

# insert_into(
#     sql_runner=sql_runner,
#     table_name="YourTable",
#     attributes=["Attr1", "Attr4", "Attr5"],
#     values=[4, 2, 2],
# )

# insert_into(
#     sql_runner=sql_runner,
#     table_name="YourTable",
#     attributes=["Attr1", "Attr4"],
#     values=[2, 4],
# )

# print("Select A")
# A = my_select(sql_runner=sql_runner, table_name="MyTable", attributes=["Attr1", "Attr3"])

# print("Select B")
# B = my_select(sql_runner=sql_runner, table_name="YourTable", attributes=["*"])

# D = merge_join(A, B, attributes=["Attr1"], mode=JoinMode.inner_join)
# D = merge_join(A, B, attributes=["Attr1"], mode=JoinMode.left_outer_join)
# D = merge_join(A, B, attributes=["Attr1"], mode=JoinMode.right_outer_join)
# D = merge_join(A, B, attributes=["Attr1"], mode=JoinMode.full_outer_join)
# D = merge_join(B, A, attributes=["Attr1"], mode=JoinMode.inner_join)
# D = merge_join(B, A, attributes=["Attr1"], mode=JoinMode.left_outer_join)
# D = merge_join(B, A, attributes=["Attr1"], mode=JoinMode.right_outer_join)
# D = merge_join(B, A, attributes=["Attr1"], mode=JoinMode.full_outer_join)

# from sql_parser import input_sql, SQLType

# while True:
#     type, args = input_sql()
#     if type == SQLType.CREATE:
#         table_name, attributes, primary_key = args
#         df = create_table(sql_runner=sql_runner, table_name=table_name, attributes=attributes, primary_key=primary_key)
#     elif type == SQLType.INSERT:
#         table_name, attributes, values = args
#         df = insert_into(sql_runner=sql_runner, table_name=table_name, attributes=attributes, values=values)
#     elif type == SQLType.DELETE:
#         table_name, conditions = args
#         df = delete_from(sql_runner=sql_runner, table_name=table_name, conditions=conditions)
#     elif type == SQLType.DROP:
#         table_name = args
#         df = drop_table(sql_runner=sql_runner, table_name=table_name)
#     elif type == SQLType.SELECT:
#         table_name, attributes, conditions = args
#         df = my_select(sql_runner=sql_runner, table_name=table_name, attributes=attributes, conditions=conditions)
#     else:
#         break
#     print(df)


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
