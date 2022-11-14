# Что такое глубокая и поверхностная копия
# значение переменной хранится в RAM - оператива
# todo поверхностная копия
from typing import Union

int1 = 12  # ссылка на область в памяти
int2 = int1  # ссылка на переменную

dict1 = {"age": 18}  # ссылка на область в памяти
dict2 = dict1  # ссылка на переменную
dict3 = dict2

dict1["age"] = 17

# print(dict1)
# print(dict2)
# print(dict3)
# todo глубокая копия
dict4 = {"age": 18}  # ссылка на область в памяти
dict5 = dict4.copy()

dict4["age"] = 17
# print(dict4)
# print(dict5)

# JIT - just in time comp...
# Чем файл .рус отличается от .ру?
# TODO .рус - "скомпилированные" файлы .ру

# Linux
# +: $ цена, производительность, безопасность
# -: сложность
# виртуальную машину (vmware / vbox) или полностью установить на пк/ноут

# GIT (open source) - система контроля версий
# git init / git pust / git merge / add....
# GITHUB (microsoft) - облачная система хранения версий под гит (GITLAB)
# создаётся скрытая папка с файлами внутри, которая следит за изменениями всех ваших файлов
# инкрементное - добавляется к предыдущему
# env / node_modules ...

# Что такое *args и **kwargs
# args - позиционные - tuple - кортеж
# kwargs - именные - dict - словарь
print(*(1, 2, 3))  # ручная распаковка
tup1 = (1, 2, 3)
a, b, c = tup1  # автораспаковка


def summing(a1, b1):
    return a1 + b1


def summing2(*args):
    res = 0
    for i in args:
        res += i
    return res


print(summing2(15, 15, 15))


def summing3(**kwargs):
    res = 0
    for k, v in kwargs.items():
        res += v
    return res


# print(summing3(**{"val1": 20, "val2": 20, "val3": 20}))
print(summing3(val1=20, val2=20, val3=20))


def print1(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


print1(12, 1123, name="Привет")


# аннотация типов
# строгой типизацией (c++ / c / c# / java)
# динамической (слабая / сильная) типизацией (javascript / python / php)

def summing7(a2: float, b2: float) -> Union[float, int]:
    return a2 + b2


print(12 / summing7(1, 2))


print(*(12, 15))
print(12, 15)

dict1 = {"age": 12, "age2": 15}
print(dict1["age2"])
for key in dict1.keys():
    print(key)  # age age2
for value in dict1.values():
    print(value)  # 12 15
for item in dict1.items():  # key, value = item
    print(item)  # ("age", 12) ("age2", 15)
print({"age": 12, "age2": 15}.keys())
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(*dict1)
# print(**dict1)
print(age=12, age2=15)
