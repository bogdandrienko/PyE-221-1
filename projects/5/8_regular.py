import hashlib

txt = r"(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$"
txt2 = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

input_from_user1 = "qwerty"
input_from_user1.isascii()  # пароль должен быть на английском
input_from_user1.isascii()  # пароль должен сод

# Минимум восемь символов, минимум одна заглавная буква, одна строчная буква и одна цифра:

input_from_user2 = "12345qwerty"

# a = input("124124?")

r"^   (?=.*[a-z])  (?=.*[A-Z])  (?=.*\d)   [A-Z a-z 0-9 \d]  {8,16}  $"
b = "124124"
# Хотя бы одна заглавная английская буква ,(?=.*?[A-Z])
# Хотя бы одна строчная английская буква,(?=.*?[a-z])
# Хотя бы одну цифру,(?=.*?[0-9])
# По крайней мере, один специальный символ,(?=.*?[#?!@$%^&*-])
# Минимум восемь в длину .{8,}(с анкерами)

# @ .com / .ru

import re

regex = r'^       [a-z0-9] + [\._]?[a-z0-9]    + [@]\w  + [.]\w    {2,3}       $'


def check(email):
    our_regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    email = email
    result = re.search(pattern=our_regex, string=email)

    print(result)
    if re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
        print("Почта верная")
    else:
        print("Почта не верная, повторите")


# либо бесконечный цикл, либо рекурсия

check('bogdanrienko@gmail.com')


# пароль

def sum1(a2: int, b2: int) -> int:
    return a2 + b2


def summary() -> None:
    try:
        a1 = input("Введите число а1:")  # python
        b1 = input("Введите число b1:")  # python
        print(sum1(int(a1), int(b1)))
    except:
        print("\n\nОшибка ввода, повторите ввод!\n")
        summary()


# summary()

# while True:
#     # isinstance(1.0, int)
#     # type(1) ==
#     a1 = input("Введите число а1:")  # python
#     if not re.search(r'^\d+$', a1):
#         print("\n\nОшибка ввода, повторите ввод!\n")
#         continue
#     b1 = input("Введите число b1:")  # python
#     if not re.search(r'^\d+$', b1):
#         print("\n\nОшибка ввода, повторите ввод!\n")
#         continue
#     print(sum1(int(a1), int(b1)))
#     break

while True:
    a1 = input("Введите новый пароль:")  # python
    if not re.search(r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", a1):
        print("\n\nОшибка ввода, повторите ввод!\n")
        continue
    b1 = input("Введите новый пароль ещё раз:")  # python
    if a1 != b1:
        print("\n\nОшибка ввода, повторите ввод!\n")
        continue
    print(hashlib.sha512(b1.encode()))
    break

p = re.compile('^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?')
