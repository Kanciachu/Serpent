from enum import Enum

class Token:
    def __init__(self, typee, value=None):
        self.type = typee
        self.value = value

    def __repr__(self):
        if self.value:
            return f"{self.type}:{self.value}"
        else:
            return f"{self.type}"


class TokenType(Enum):
    INT = "INT"
    FLOAT = "FLOAT"
    STRING = "STRING"
    IDENTIFIER = "IDENTIFIER"
    KEYWORD = "KEYWORD"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLICATION = "MUL"
    DIVISION = "DIV"
    EXCLAMATION_EQUALS = "EXCLAMATION EQUALS"
    LEFT_PARAN = "LEFT PARAN"
    RIGHT_PARAN = "RIGHT PARAN"
    EQUAL_EQUAL = "EQUAL EQUAL"
    NOT_EQUAL = "NOT EQUAL"
    LESSER = "LESSER THAN"
    GREATER = "GREATER THAN"
    LESSER_EQUAL = "LESSER EQUAL"
    GREATER_EQUAL = "GREATER EQUAL"
    EOF = "EOF"

class Keywords(Enum):
    AND = "AND"
    NOT = "NOT"
    OR = "OR"
