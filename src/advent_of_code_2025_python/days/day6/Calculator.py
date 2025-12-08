from functools import reduce
from operator import mul, add


class Calculator:

    def __init__(self, values: list[str], operator: str):
        self._values = values
        if operator == "*":
            self._operator = mul
            self._default_value = 1
        else:
            self._operator = add
            self._default_value = 0

    def solve(self):
        return reduce(lambda acc, val: self._operator(acc, int(val)), self._values, self._default_value)

    def solve_right_left(self):
        transposed = list(zip(*self._values))
        return reduce(lambda acc, val: self._operator(acc, int("".join(val))), transposed, self._default_value)