def parse_select(sql: str) -> tuple:
    from sql_parser.parse_conditions import parse_conditions

    sql = sql[6:-1]
    if sql.find("where") != -1:
        sql, conditions = sql.split("where")
        conditions = conditions.strip()
        conditions = parse_conditions(conditions=conditions)
    else:
        conditions = None
    attributes, tables = sql.strip().split("from")
    attributes = attributes.strip().split(",")
    tables = tables.strip().split(",")
    attributes = [attribute.strip() for attribute in attributes]
    tables = [table.strip() for table in tables]
    return tables, attributes, conditions
