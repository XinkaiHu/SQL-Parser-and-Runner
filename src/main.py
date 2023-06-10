from sql_runner import SQLRunner
from init_meta import init_meta
from create_table import create_table
from insert_into import insert_into
from delete_from import delete_from
from select import select
from merge_join import merge_join, JoinMode

sql_runner = SQLRunner(database_name="MyDatabase")

init_meta(sql_runner=sql_runner)

create_table(
    sql_runner=sql_runner,
    table_name="MyTable",
    attributes=["Attr1", "Attr2", "Attr3"],
    primary_key="Attr1",
)

create_table(
    sql_runner=sql_runner,
    table_name="YourTable",
    attributes=["Attr1", "Attr4", "Attr5"],
    primary_key="Attr1",
)

insert_into(
    sql_runner=sql_runner,
    table_name="MyTable",
    attributes=["Attr1", "Attr2", "Attr3"],
    values=[1, 2, 3],
)

insert_into(
    sql_runner=sql_runner,
    table_name="MyTable",
    attributes=["Attr1", "Attr2"],
    values=[2, 4],
)

insert_into(
    sql_runner=sql_runner,
    table_name="MyTable",
    attributes=["Attr1", "Attr2", "Attr3"],
    values=[3, 2, 4],
)

insert_into(
    sql_runner=sql_runner,
    table_name="YourTable",
    attributes=["Attr1", "Attr4", "Attr5"],
    values=[1, 2, 2],
)

insert_into(
    sql_runner=sql_runner,
    table_name="YourTable",
    attributes=["Attr1", "Attr4", "Attr5"],
    values=[4, 2, 2],
)

insert_into(
    sql_runner=sql_runner,
    table_name="YourTable",
    attributes=["Attr1", "Attr4"],
    values=[2, 4],
)

A = select(sql_runner=sql_runner, table_name="MyTable", attributes=["Attr1", "Attr3"])

B = select(sql_runner=sql_runner, table_name="YourTable", attributes=["Attr1", "Attr4", "Attr5"])

D = merge_join(A, B, attributes=["Attr1"], mode=JoinMode.inner_join)
D = merge_join(A, B, attributes=["Attr1"], mode=JoinMode.left_outer_join)
D = merge_join(A, B, attributes=["Attr1"], mode=JoinMode.right_outer_join)
D = merge_join(A, B, attributes=["Attr1"], mode=JoinMode.full_outer_join)
D = merge_join(B, A, attributes=["Attr1"], mode=JoinMode.inner_join)
D = merge_join(B, A, attributes=["Attr1"], mode=JoinMode.left_outer_join)
D = merge_join(B, A, attributes=["Attr1"], mode=JoinMode.right_outer_join)
D = merge_join(B, A, attributes=["Attr1"], mode=JoinMode.full_outer_join)
