from token import Token, TokenType, Keywords
from parser import Parser


class Scaner:
    def __init__(self, text):
        self.text = text
        self.current_char = None
        self.position = -1
        self.next()

    def next(self):

        """ Moves position of scaner by one, if there are no chars left it returns none """

        self.position += 1
        if len(self.text) > self.position:
            self.current_char = self.text[self.position]
        else:
            self.current_char = None

    def create_tokens(self):

        """Hearth of whole scaner it selects chars from text and divides them into categories """

        tokens = []

        while self.current_char is not None:

            match self.current_char:
                case " " | "\t":
                    self.next()
                case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
                    tokens.append(self.create_number_token())
                case "-":
                    tokens.append(Token(TokenType.MINUS.value))
                    self.next()
                case "+":
                    tokens.append(Token(TokenType.PLUS.value))
                    self.next()
                case "/":
                    tokens.append(Token(TokenType.DIVISION.value))
                    self.next()
                case "*":
                    tokens.append(Token(TokenType.MULTIPLICATION.value))
                    self.next()
                case ")":
                    tokens.append(Token(TokenType.RIGHT_PARAN.value))
                    self.next()
                case "(":
                    tokens.append(Token(TokenType.LEFT_PARAN.value))
                    self.next()
                case "=":
                    print()
                    if self.text[self.position + 1] == "=":
                        tokens.append(Token(TokenType.EQUAL_EQUAL.value))
                        self.next()
                    self.next()
                case "!":
                    if self.text[self.position + 1] == "=":
                        tokens.append(Token(TokenType.EXCLAMATION_EQUALS.value))
                        self.next()
                    self.next()
                case ">":
                    if self.text[self.position + 1] == "=":
                        tokens.append(Token(TokenType.GREATER_EQUAL.value))
                        self.next()
                    else:
                        tokens.append(Token(TokenType.GREATER.value))
                    self.next()
                case "<":
                    if self.text[self.position + 1] == "=":
                        tokens.append(Token(TokenType.LESSER_EQUAL.value))
                        self.next()
                    else:
                        tokens.append(Token(TokenType.LESSER.value))
                    self.next()
                case "A":
                    if self.text[self.position + 1] == "N" and self.text[self.position + 2] == "D":
                        tokens.append(Token(Keywords.AND.value))
                        self.next()
                        self.next()
                    self.next()
                case "N":
                    if self.text[self.position + 1] == "O" and self.text[self.position + 2] == "T":
                        tokens.append(Token(Keywords.NOT.value))
                        self.next()
                        self.next()
                    self.next()
                case "O":
                    if self.text[self.position + 1] == "R":
                        tokens.append(Token(Keywords.OR.value))
                        self.next()
                    self.next()
                case _:
                    print(f"Error occurred line : {self.position} ")
                    return []


        # tokens.append(Token(TokenType.EOF))
        return tokens

    def create_number_token(self):

        """ Function creates number token both integers and float types """

        dot_flag = False
        num = ""

        while self.current_char is not None and self.current_char in list("1234567890."):
            if self.current_char == ".":
                if dot_flag:
                    break
                else:
                    dot_flag = True
                    num += "."
            else:
                num += self.current_char
            self.next()
        if dot_flag:
            return Token(TokenType.FLOAT.value, float(num))
        else:
            return Token(TokenType.INT.value, int(num))

    def start(self, text):

        """ This functions starts a scaner """

        # SCANER GENERATES TOKENS

        scaner = Scaner(text)
        tokens = scaner.create_tokens()

        # PARSER GENERATES ABSTRACT SYNTAX TREE

        parser = Parser(tokens)
        ast = parser.parse()

        return ast
