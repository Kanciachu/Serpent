class Number:
    def __init__(self, value):
        self.value = value

    def sub(self, comp):
        if type(self) == type(comp):
            return Number(self.value - comp.value)

    def add(self, comp):
        if type(self) == type(comp):
            return Number(self.value + comp.value)

    def div(self, comp):
        if type(self) == type(comp):
            if self.value == 0 or comp.value == 0:
                print("Division by zero!!!")
            else:
                return Number(self.value / comp.value)

    def mul(self, comp):
        if type(self) == type(comp):
            return Number(self.value * comp.value)

    def com_eq(self, comp):
        if type(self) == type(comp):
            return Number(int(self.value == comp.value))

    def com_ne(self, comp):
        if type(self) == type(comp):
            return Number(int(self.value != comp.value))

    def com_lt(self, comp):
        if type(self) == type(comp):
            return Number(int(self.value < comp.value))

    def com_gt(self, comp):
        if type(self) == type(comp):
            return Number(int(self.value > comp.value))

    def com_lte(self, comp):
        if type(self) == type(comp):
            return Number(int(self.value <= comp.value))

    def com_gte(self, comp):
        if type(self) == type(comp):
            return Number(int(self.value >= comp.value))

    def and_op(self, comp):
        if type(self) == type(comp):
            return Number(int(self.value and comp.value))

    def or_op(self, comp):
        if type(self) == type(comp):
            return Number(int(self.value or comp.value))

    def not_op(self):
        a = 0
        if self.value == 0:
            a = 1
        return Number(a)

    def __repr__(self):
        return str(self.value)