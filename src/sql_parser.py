def parse_select(sql: str) -> tuple:
    sql = sql.lower().strip()[6:]
    if sql.endswith(";"):
        sql = sql[:-1]
    if sql.find("where"):
        sql, conditions = sql.split("where")
        conditions = conditions.strip()
    else:
        conditions = None
    attributes, tables = sql.strip().split("from")
    attributes = attributes.strip().split(",")
    tables = tables.strip().split(",")
    attributes = [attribute.strip() for attribute in attributes]
    tables = [table.strip() for table in tables]
    return tables, attributes, conditions

print(parse_select("select * from table where a > 0;"))


def parse_insert_into(sql: str) -> tuple:
    sql = sql.lower().strip()