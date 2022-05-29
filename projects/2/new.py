# TODO типы данных
# целочисленные - 1, 3, 5, -10, 0
value_1 = 10
value_2 = -10
value_3 = 0
value_4 = int(10.5)  # 10
value_5 = int("10")  # 10

print(type(value_1))  # <class 'int'>

# с плавающей точкой - 1, 3, 5, -10, 0

value_1_1 = 10.1
value_2_1 = -10.4
value_3_1 = 0.0
value_4_1 = float(10)  # 10.0

print(type(value_1_1))  # <class 'float'>

# boolean  - логическая(булевая) переменная - Правда / Ложь
value_1_2 = True
value_2_2 = False
value_3_2 = bool(0)  # False
value_4_2 = bool("123123")  # True

print(type(value_1_2))  # <class 'bool'>

# символьные значения - строковые
value_1_3 = ""
value_2_3 = "12"
value_3_3 = "12.5"
value_4_3 = "Many яблок"
value_5_3 = str(10)  # "10"

print(type(value_4_3))  # <class 'str'>

# список(массив) - содержит другие типы данных

value_1_4 = ["", "12", 12, 15.6, -100, [False]]
value_2_4 = []
value_3_4 = list("12")  # ["12"]

print(type(value_1_4))  # <class 'list'>

# кортеж(массив) - содержит неизменяемый тип данных

value_1_5 = ("", "12", 12, 15.6, -100, [False])
value_2_6 = (12,)
value_3_6 = tuple("12")  # ("12",)

print(type(value_2_6))  # <class 'tuple'>

# словарь - содержит пары значений в формате ключ-значение

value_1_6 = {}
value_2_6 = {"key_1": "value_1", 12: 12, 12.5: 14.5}
value_3_6_1 = dict(key_1="value_1")  # конструктор

print(type(value_2_6))  # <class 'dict'>

# TODO условные операторы

# if (логическая переменная):
#   операции, если логическая переменная == True


# if (логическая переменная):
#   операции, если логическая переменная == True
# else:
#   операции, если логическая переменная == False

value_bool_1 = True

if value_bool_1:
    print("Правда 1")

value_bool_2 = False

if value_bool_2:
    print("Правда 2")
else:
    print("Ложь 2")

# TODO циклы

# перечисляемый цикл, или цикл-for
# for (переменная, которая будет содержать каждый раз разное значение из итератора) in (итератор - объект по которому проходимся циклом)
#    (логика, которая выполняется каждую итерацию - повторение цикла)

#         0  1  2  3  4
for i in [2, 3, 4, 5, 6]:
    print(i)

str_value_4_3 = "! Many яблок !"
for char_element in str_value_4_3:
    print(char_element)

str_value_4_3 = "! Many яблок !"
for first_loop in [["1_1", "1_2", "1_3", "1_4", "1_5"], ["2_1", "2_2", "2_3", "2_4", "2_5"]]:
    # Вторая итерация(повторение цикла) не запускается, пока вложенный цикл не отработает полностью
    for second_loop in first_loop:
        print(second_loop)

# условный цикл while("пока")


while_continie = True
index = 0
while while_continie:
    index = index + 2
    print(index)
    # index += 2
    if index >= 30:
        # break
        while_continie = False

from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
