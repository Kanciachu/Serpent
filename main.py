from scaner import Scaner
from parser import Parser
from interpreter import Interpreter
from token import TokenType, Keywords

while True:
    text = input(">")
    scaner = Scaner(text)
    tokens = scaner.create_tokens()

    parser = Parser(tokens)
    ast = parser.parse()

    interpreter = Interpreter()
    result = interpreter.visit(ast)

    print(result)