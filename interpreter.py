from values import Number
from token import TokenType, Keywords


class Interpreter:
    def visit(self, ast):
        match type(ast).__name__:
            case "BinaryOperation":
                result = self.visit_binary_operation(ast)
            case "UnaryOperation":
                result = self.visit_unary_operation(ast)
            case "Number":
                result = self.visit_number(ast)
            case _:
                self.visit_error()

        return result

    def visit_error(self):
        print(" INTERPRETER ERROR ")

    def visit_binary_operation(self, ast):
        outcome = 0
        left = self.visit(ast.left_token)
        right = self.visit(ast.right_token)

        match str(ast.operation_token):
            case TokenType.MINUS.value:
                outcome = left.sub(right)
            case TokenType.PLUS.value:
                outcome = left.add(right)
            case TokenType.DIVISION.value:
                outcome = left.div(right)
            case TokenType.MULTIPLICATION.value:
                outcome = left.mul(right)
            case TokenType.EQUAL_EQUAL.value:
                outcome = left.com_eq(right)
            case TokenType.NOT_EQUAL.value:
                outcome = left.com_ne(right)
            case TokenType.LESSER.value:
                outcome = left.com_lt(right)
            case TokenType.GREATER.value:
                outcome = left.com_gt(right)
            case TokenType.GREATER_EQUAL.value:
                outcome = left.com_gte(right)
            case TokenType.LESSER_EQUAL.value:
                outcome = left.com_lte(right)
            case Keywords.AND.value:
                outcome = left.and_op(right)
            case Keywords.OR.value:
                outcome = left.or_op(right)
        return outcome

    def visit_unary_operation(self, ast):
        number = self.visit(ast.token)

        if str(ast.operation_token) == TokenType.MINUS.value:
            number = number.mul(Number(-1))
        elif str(ast.operation_token) == Keywords.NOT.value:
            number = number.not_op()

        return  number



    def visit_number(self, ast):
        return Number(ast.token.value)

