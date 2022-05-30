class Number:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f"{self.token}"


class BinaryOperation:
    def __init__(self, left_token, operation_token, right_token):
        self.left_token = left_token
        self.operation_token = operation_token
        self.right_token = right_token

    def __repr__(self):
        return f"({self.left_token}, {self.operation_token}, {self.right_token})"

class UnaryOperation:
    def __init__(self, operation_token, token):
        self.operation_token = operation_token
        self.token = token

    def __repr__(self):
        return f"({self.operation_token}, {self.token})"
