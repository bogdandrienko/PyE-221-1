# https://intellipaat.com/blog/interview-question/python-interview-questions/
# https://www.interviewbit.com/python-interview-questions/
# https://techrocks.ru/2020/10/10/100-python-questions-for-tech-interview/
from _decimal import Decimal

########################################################################################################################

# What is Python?
# Динамический интерпретируемый язык программирования с сборщиком мусора

########################################################################################################################

# Python is an interpreted language. Explain
# compile (binary-file) превращается в байт код (C++ / Go) vs interpreted (.py) читается "на лету" (Python / JavaScript)

########################################################################################################################

# What is the difference between lists and tuples?
# изменяемый vs не изменяемый, методы, потребление памяти

########################################################################################################################

# What is pep 8?
# "соглашение" программистов на Python, где они описывают стиль написания кода

########################################################################################################################

# What are the Key features of Python?
# Лёгкий синтаксис, быстрая разработка и прототипирование, много библиотек (numpy, plot, keras, opencv, tensor...)

########################################################################################################################

# How is Memory managed in Python?
# automatic - есть "область видимости" сборщик мусора следит за ссылками на объекты, если на объект нет ссылок - очистка

########################################################################################################################

# What is PYTHONPATH?
# путь к интерпретатору

########################################################################################################################

# What are Python Modules?
# пакеты или библиотеки с чужим кодом (pip.org)

########################################################################################################################

# What are python namespaces?
# области видимости: глобальная, блочная(локальная)
name = "Sholpan"  # global


def func1():
    global name
    name = "Dimash"  # local func1

    def func2():
        name = "Dimash"  # local func2


print(name)
func1()
print(name)


########################################################################################################################

# Explain Inheritance in Python with an example?
# Inheritance - наследование в Python: множественное и одиночное | django - mixins (class based view - authrequired)

# todo simple Inheritance
class Mother1:  # (object)
    color_eyes = "blue"


class Child1(Mother1):  # (object)
    # color_eyes = "blue"
    pass


ch1 = Child1()
print(ch1.color_eyes)


# todo complex(many) Inheritance

class Mother2:  # (object)
    color_eyes = "blue"


class Father2:  # (object)
    color_eyes = "brown"


class Child2(Mother2, Father2):  # left - to - right priority
    # color_eyes = "blue"
    pass


ch2 = Child2()
print(ch2.color_eyes)

########################################################################################################################

# What are the common built-in data types in Python?
# типы данных
a: int = 12
b: float = 12.014151235252452452452345
c: Decimal = Decimal(12.014151235252452452452345415145)
d: bool = True
e: dict[str, int] = {"age": 22}
f: list = [1, 2, 3]

########################################################################################################################

# What is the Difference Between a Shallow Copy and Deep Copy?

dict1 = {"name": "Sholpan"}
print(dict1)
dict2 = dict1  # Shallow Copy (поверхностная) - на самом деле тут лежит ссылка на первый объект
dict1["name"] = "Dimash"
print(dict1)
print(dict2)

dict3 = {"name": "Sholpan"}
print(dict3)
dict4 = dict3.copy()  # Deep Copy (глубокая) - полное копирование
dict3["name"] = "Dimash"
print(dict3)
print(dict4)


def start():
    dict2 = {"password": "Qwertty!"}

    def change(dict1: dict) -> dict:
        temp_dict = {"name": 12}
        dict1["name"] = 12
        # dict1["password"] = ""
        # del dict1["password"]
        return temp_dict

    change(dict2)
    print(dict2)

    dict3 = change(dict2.copy())
    print(dict3)
    print(dict2)


start()
