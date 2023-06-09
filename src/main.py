from sql_runner import SQLRunner
from init_meta import init_meta
from create_table import create_table
from insert_into import insert_into
from delete_from import delete_from
from select import select

sql_runner = SQLRunner(database_name="MyDatabase")

init_meta(sql_runner=sql_runner)

create_table(
    sql_runner=sql_runner,
    table_name="MyTable",
    attributes=["Attr1", "Attr2", "Attr3"],
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

delete_from(
    sql_runner=sql_runner, table_name="MyTable", conditions=("Attr2", lambda x: x == 2)
)

select(sql_runner=sql_runner, table_name="MyTable", attributes=["Attr1", "Attr3"])
