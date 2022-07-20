# def calc1():
#     return 2 * 2
#
#
# res1 = calc1()
# print(res1)
#
#
# def calc2(value):
#     return 2 * value
#
#
# res2 = calc2(3)
# print(res2)
#
# calc3 = lambda x: x * 2
#
# value = [
#     {"title": }
# ]

# Нахождение факториала числа
# Палиндром  -  "мадам"  - "анна"  - "роза упала на лапу азора"  # "{([)}"

b = """
А муза рада музе без ума да разума
или
"""

a = """
голод долог
"""


# def get_value(val1):
#     if val1 < 10:
#         return True
#     else:
#         get_value(val1-1)

# def get_factorial(num: int):
#     if num <= 0:
#         return True
#     else:
#         print(num * 2)
#         get_factorial(num - 1)
#
# get_factorial(5)

def is_palindrome(s):
    if len(s) < 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


def is_palindrom(text: str):  # return True if text is palindrom bla-bla
    if len(text) < 1:
        return True
        # continue break
    if text[0] == text[-1]:  # text[-1]: - предпоследний           text[len(text)]: - последний
        return is_palindrom(text[1:-1])  # ада   [0:len(new_text):1]
    else:
        return False


# is_palindrom(s: str) -> True/False  -> is_palindrom(s: str) -> True/False -> is_palindrom(s: str) -> True/False ...
# is_palindrom(s: str) -> True/False  -> is_palindrom(s: str) -> True/False <- is_palindrom(s: str) <- True

def is_palindrom2(text1: str):
    text2 = text1[::-1]
    print(text1)
    print(text2)
    if text1 == text2:  # t "158" <=> t "158"
        # ord()
        return True
    else:
        return False


res = is_palindrom2("Мадам")
print(res)
print(type(res))
if res:
    print("Да, это палиндром")
else:
    print("Нет, это  не палиндром")

# callback


exprs1 = lambda val1, val2: val1 * val2  # лямбда выражение


def calc1(val1, val2):
    return val1 * val2


exprs2 = calc1  # ссылка на функцию

print(exprs1(2, 7))
print(exprs2(2, 7))

arr1 = []
for i in range(1, 5):
    if i % 2 == 0:
        # result = calc1(12, i)
        arr1.append(exprs1)
    else:
        arr1.append(calc1)

print(arr1)
print(type(arr1))

print(arr1[0])
print(type(arr1[0]))

for i in arr1:
    print(i(1, 2))


# lam1 = lambda character: ord(character)

# print(lam1())

def lam2(character):
    return ord(character)


lam1 = lambda character: ord(character)

arrrr1 = [lam1(x) for x in 'Привет мир!']  # lazy computing
print(arrrr1)

arrrr1 = [8, *arrrr1, 8]  # *args - позиционные аргументы

for i in arrrr1:
    print(i)

print(arrrr1)
# arrrr1.sort(key=lambda item: str(item).find("8"), reverse=True)
arrrr1.sort(key=lambda item: item % 2 == 0, reverse=False)  # от меньшего к большему 0....9...100

#    2    2      2    2     2    0  0     -1    -1     -1    -1  -1  -1
# '1088'
# [1088, 1080, 1084, 1080, 1088, "8", 8, 1055, 1074, 1077, 1090, 32, 33]
print(arrrr1)

