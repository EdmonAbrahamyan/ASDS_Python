class Calculation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y


class MyCalculation(Calculation):
    def __init(self, x, y):
        Calculation.__init__(self, x, y)

    def multiplication(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y

my_calc = MyCalculation(3, 5)

print(f"addition of {my_calc.x} and {my_calc.y} is ", my_calc.addition())
print(f"subtraction of {my_calc.x} and {my_calc.y} is ", my_calc.subtraction())
print(f"multiplication of {my_calc.x} and {my_calc.y} is ", my_calc.multiplication())
print(f"division of {my_calc.x} and {my_calc.y} is ", my_calc.division())
