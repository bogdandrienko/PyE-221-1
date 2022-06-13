import openpyxl
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

filename = 'users.xlsx'
filedir = 'home_work'

workbook = openpyxl.load_workbook(filedir + "/" + filename)
worksheet = workbook.active

max_row = worksheet.max_row
max_column = worksheet.max_column

workers = []


class Worker:  # определение (создание базовых параметров) класса
    def __init__(self, first_name: str, second_name: str, patronymic: str, position,
                 category="Рабочий"):  # магический метод для инициализации (создания) класса
        self.value_first_name = first_name  # свойство (переменная) внутри класса - изменяемая
        self.value_second_name = second_name  # свойство (переменная) внутри класса - изменяемая
        self.value_patronymic = patronymic  # свойство (переменная) внутри класса - изменяемая
        self.value_position = position  # свойство (переменная) внутри класса - изменяемая
        self.value_category = category  # свойство (переменная) внутри класса - изменяемая

        self.radius = 0

    def print_full_name(self):
        print(f'{self.value_second_name} {self.value_first_name}')

    def get_full_name(self):
        return f'{self.value_second_name} {self.value_first_name}'

    def calcuate(self, side=14):
        self.radius = side ** 2


for row in range(1, max_row + 1):
    worker = []

    for column in range(1, 5 + 1):
        obj = worksheet.cell(row=row, column=column)  # метод (функция в классе) который получает объект по координатам
        # print(obj)
        # print(type(obj))

        value = obj.value  # свойство (переменная в классе) которое получает значение ячейки

        if not value:
            value = ''
        worker.append(value)

    # print(worker)
    # print('читаю нового работника!')
    worker_obj = Worker(
        first_name=worker[1],
        second_name=worker[0],
        patronymic=worker[2],
        position=worker[3],
        category=worker[4],
    )

    # worker_obj.print_full_name()
    full_name = worker_obj.get_full_name()
    # print(full_name)

    workers.append(worker_obj)
    # workers.append(worker)
# print(workers)

print(workers[1].value_patronymic)

print(f'{workers[1].value_second_name} {workers[1].value_first_name}')  # Исагулов  Куаныш
workers[1].print_full_name()  # Исагулов  Куаныш
print(workers[1].get_full_name())  # Исагулов  Куаныш

external_value_variable = 1

workbook = Workbook()
print(workbook)
print(type(workbook))


class CustomWorkerClass1:  # определение (создание базовых параметров) класса
    def __init__(self):  # магический метод для инициализации (создания) класса
        self.VALUE_CONSTANT = 321  # свойство (переменная) внутри класса - константа (не изменяется)


print(CustomWorkerClass1)
print(type(CustomWorkerClass1))

worker = CustomWorkerClass1()  # создание экземпляра класса CustomWorkerClass
print(worker)
print(type(worker))
print(worker.VALUE_CONSTANT)  # получение свойства данного экземпляра данного класса


class CustomWorkerClass2:  # определение (создание базовых параметров) класса
    def __init__(self, external_value_variable2=15):  # магический метод для инициализации (создания) класса
        self.VALUE_CONSTANT = 321  # свойство (переменная) внутри класса - константа (не изменяется)
        self.value_variable = external_value_variable2  # свойство (переменная) внутри класса - изменяемая


worker = CustomWorkerClass2(external_value_variable2=156)  # создание экземпляра класса CustomWorkerClass
print(worker)
print(type(worker))
print(worker.VALUE_CONSTANT)  # получение свойства данного экземпляра данного класса
print(worker.value_variable)  # получение свойства данного экземпляра данного класса

print("\n\n\n**********\n\n\n")


# класс для расчёта периметров и площадей
class MyClass:
    def __init__(self, name: str, side1: float, side2: float, side3: float, side4: float):
        self.name = name
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

        self.radius = 0

    def print_name(self):
        print(self.name)

    def get_perimeter(self):
        perimeter_value = self.side1 + self.side2 + self.side3 + self.side4
        return perimeter_value

    def calcuate(self, side=14):
        self.radius = side ** 2


figure1 = MyClass(name="квадрат", side4=10, side2=10, side3=10, side1=10)  # квадрат
figure1.print_name()
square_perimeter = figure1.get_perimeter()
print(square_perimeter)
