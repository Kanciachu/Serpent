from token import TokenType, Keywords
from nodes import Number, BinaryOperation, UnaryOperation


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.position = -1
        self.next()

    def parse(self):
        result = self.expression()
        return result

    def next(self):

        """ Returns next token if there is another """

        self.position += 1
        if len(self.tokens) > self.position:
            self.current_token = self.tokens[self.position]
        return self.current_token

    def expression(self):

        """ EXPRESSION ---> TERM (( + | - ) ,TERM) * """

        return self.binary_operation(self.comparison, (Keywords.AND.value, Keywords.OR.value))

    def term(self):

        """ TERM ---> FACTOR(( / | * ) FACTOR) * """

        return self.binary_operation(self.factor, (TokenType.MULTIPLICATION.value, TokenType.DIVISION.value))

    def arith_expr(self):

        """"""

        return self.binary_operation(self.term, (TokenType.PLUS.value, TokenType.MINUS.value))

    def factor(self):

        """ FACTOR ---> [  INT  |  FLOAT  ]
                   ---> (  +  | -  ) FACTOR
                   ---> ( ( EXPRESSION ) ) """

        token = self.current_token
        if token.type == TokenType.PLUS.value or token.type == TokenType.MINUS.value:
            self.next()
            factor = self.factor()
            return UnaryOperation(token, factor)

        elif token.type == TokenType.INT.value or token.type == TokenType.FLOAT.value:
            self.next()
            return Number(token)

        elif token.type == TokenType.LEFT_PARAN.value:
            self.next()
            ekspresja = self.expression()
            if self.current_token.type == TokenType.RIGHT_PARAN.value:
                self.next()
                return ekspresja
            else:
                print("Error expected [ ) ] ")

    def comparison(self):


        if self.current_token == str(Keywords.NOT.value):
            operation_token = self.current_token
            self.next()

            temp = self.comparison()
            return UnaryOperation(operation_token, temp)

        return self.binary_operation(self.arith_expr,(TokenType.LESSER_EQUAL.value,
                                                      TokenType.GREATER_EQUAL.value,
                                                      TokenType.LESSER.value,
                                                      TokenType.GREATER.value,
                                                      TokenType.NOT_EQUAL.value,
                                                      TokenType.EQUAL_EQUAL.value))

    def binary_operation(self, function, operator):

        left_token = function()

        while self.current_token.type in operator:
            operation_token = self.current_token
            self.next()
            right_token = function()
            left_token = BinaryOperation(left_token, operation_token, right_token)

        return left_token