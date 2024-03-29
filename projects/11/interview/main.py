# https://intellipaat.com/blog/interview-question/python-interview-questions/
# https://www.interviewbit.com/python-interview-questions/
# https://techrocks.ru/2020/10/10/100-python-questions-for-tech-interview/
import random

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


########################################################################################################################

# Что такое инженерия и процесс разработки в целом?
# специалист, который разрабатывает системы, собирает спецификацию, перед этим проектирует их, выбирает стек технологий,
# прикидывает нагрузку, надёжность

########################################################################################################################

########################################################################################################################

# Какие знаете принципы программирования?
# flexible, refactoring (SOLID, DRY), rezistance (TDD - 95% covering) , scaling (microservise + async/thread)

########################################################################################################################

# Чем отличаются процедурная и объектно-ориентированная парадигмы программирования?
# ООП - сущности, код-полотно

########################################################################################################################

# Каковы основные принципы ООП (наследование, инкапсуляция, полиморфизм)?
# наследование - наследуем методы, свойства... от класса родителя
# инкапсуляция - сокрытие атрибутов или методов (public, _protected, __private)
# полиморфизм - переопределение нужный свойств вместо родителя

########################################################################################################################

# Что такое множественное наследование?
# class Child(Mother, Father...) - django mixins(class based view)

########################################################################################################################

# Назовите шесть этапов разработки продукта в Software Development lifecycle и расскажите, в чем разница между Agile(waterfall) и Kanban.
# Анализ, составление требований к продукту.
# Планирование.
# Проектирование и дизайн.
# Разработка.
# Тестирование.
# Развертывание, эксплуатация.

# методология - с итерациями по спринт (ограниченный feathures) - выбирают по сторипоинтам
# рефакторинг
# техдолг - технический долг

########################################################################################################################

# Какие есть методы HTTP-запросов и чем они отличаются друг от друга?
# head, options, get, post, put, patch, delete
# задачи - post добавляет "сущность", put/patch - обновление, delete - "удаляет сущность"
# get - get(/?data=12&search=python) / post (form control / json - data)

########################################################################################################################

# Как выглядят HTTP-request/response?
# пользователь -> браузер -> маршрут -> cdn -> domen names -> A row(name=ip) -> ip -> port -> ubuntu -> firewall ->
# nginx (80 http) -> nginx (443 https) -> gunicorn -> django -> django-middware -> django-urls -> django-view ->
# database <-<-<-

########################################################################################################################

# Что такое авторизация и как она работает?
# проверяет наличие тех или иных прав

########################################################################################################################

# Что такое аутентифиция и как она работает?
# определение принажлежности к аккаунту

########################################################################################################################

# Что такое cookies?
# локальное хранилище для фронтенда (есть время жизни) - / localstorage

########################################################################################################################

# Что такое веб-уязвимость?
# слабость в веб-приложении (веб-платформе), - встроенные SQL injection (форма ввода имени пользователя;drop table postgres;)
# brufors (неограниченные запросы от одного ip) / ddos - перегрузка сайта

########################################################################################################################

# What is __init__ in Python?
#

class Mother:
    def __init__(self, name):  # инициализатор
        self.name = name

    # def __new__(cls, *args, **kwargs):  # конструктор
    #     return cls(*args, **kwargs)


m1 = Mother("Erika")  # инициализация(конструкирование) класса

########################################################################################################################

# What is type conversion in Python?
# float -> int
number1 = 12.36252465536356
print(int(number1))

list1 = [1, 2, 4]
print(type(tuple(list1)))

########################################################################################################################

# What is the difference between Python Arrays and lists?
# list - different value types, встроен, slowly и large memory
# array - same(одинаковые) value types, нужно импортировать, fast
list1 = [1, 2, True, "12"]
import array

array_demo = array.array('i', [1, 2, 3, False])
print(array_demo)
array_demo.append(123)  #
print(array_demo)

########################################################################################################################

import sys

list1 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
dict1 = {"1": 1, "2": 2, "3": 3, "4": 1, "5": 2, "6": 3, "7": 1, "8": 2, "9": 3}
print(sys.getsizeof(list1))
print(sys.getsizeof(dict1))


########################################################################################################################

# Is python case sensitive?
# yes

def Func1():
    print("1")
    pass


def func1():
    print("2")
    pass


func1()
Func1()

########################################################################################################################

# What does [::-1] do?
# reverse collection
str1 = "Python"
print(str1)
print(str1[::-1])


########################################################################################################################

# В чём отличие и необходимость структур данных
# Каждая структура обладает своими свойствами, но стандартные структуры могут быть
#

# list7: list[str | int] = [1]
# list7.append(2)

class MyList(object):
    def __init__(self, *args):
        self.__store: list = [*args]
        self.__length = len(self.__store)

    def in_(self, arg):
        self.__store.append(arg)
        self.__length += 1

    def out_first(self) -> any:  # FIFO - QUEUE
        return self.__store[0]

    def out_last(self) -> any:  # LIFO - STACK
        return self.__store[len(self.__store)-1]

    def __str__(self):
        res = ""
        for i in self.__store:
            res += str(i) + " "
        return res


my1 = MyList(1, 2, 3)
my1.append(123)
print(my1)

list5 = [1, 2, 100]  # O(N) - линейная
elem = random.randint(1, 100)
for i in list5:
    if i == elem:
        print("НАШЛи")
        break

dict2 = {"1": 1, "2": 2, "3": 3}  # O(1) - константная

tree1 = []  # O(log(N))
# 1000
# 500
# 250
# 125
# 75
# 50
# 25
# 13
# 7
# 4
# 2
# 1

# https://habr.com/ru/post/188010/
