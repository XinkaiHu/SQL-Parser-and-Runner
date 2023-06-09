import re


class Predication:

    attribute: str | None = None
    operator: str | None = None
    operand: str | None = None

    def __init__(self, expression: str):

        def match_operator(expression, operator):
            op_pos = expression.find(operator)
            if op_pos != -1:
                groups = expression.split(operator)
                self.attribute = groups[0].strip()
                self.operator = operator
                self.operand = groups[-1].strip()
                print(self.attribute, self.operator, self.operand)
                return True
            else:
                return False

        operators = ["<>", "!=", "==", "<=", ">=", "=", "<", ">"]
        for operator in operators:
            if match_operator(expression=expression, operator=operator):
                break
        else:
            raise SyntaxError("No operator in expression {}".format(expression))

Predication("a <> 1")
