import openpyxl
from openpyxl import Workbook


class GrandMother:
    eyes_color = 'brown'


class Father:
    height = 180
    eyes_color = 'gray'


class Mother(GrandMother):
    __eyes_color = 'blue'

    def __init__(self, hair_color: str, multiply_value=2.0):
        self.multiply_value = multiply_value
        self.hair_color = hair_color

    def give_money(self, value: float):
        return value * self.multiply_value


class Child(Mother, Father):
    # eyes_color = 'green'

    def __init__(self, hair_color: str, multiply_value):
        super().__init__(hair_color, multiply_value)

    def give_money(self, value: float):
        return value * self.multiply_value * 1000


m1 = Mother('red', multiply_value=3)
print(m1.give_money(10))

print(isinstance(m1, Child))

if type(m1) == GrandMother:
    print('ok')
else:
    print('not ok')

# print(m1.eyes_color)


child = Child('red', multiply_value=0.5)
print(f'Child: {child._Mother__eyes_color}')
print(f'Child: {child.hair_color}')

# print(child.give_money(20))

print(child.height)

wb = Workbook()