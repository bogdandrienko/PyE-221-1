# type, input, str, abs, char, ord, encode, decode, open (with)

# DRY don't repeat yourself!

def func_print_word():  # define - определить funcPrintWord
    print('Hello world')


# func_print_word()
# func_print_word()
# func_print_word()

def func_return_word():
    return 'world!'


# result = func_return_word()
# print(result)

def func_sum_values(a, b, c):
    res = a + b + c
    return res


# result = func_sum_values(1, 2, -3)
# print(result)

def func_sum_values_with_default(a, b=3, c=10):
    res = a + b + c
    return res


# result = func_sum_values_with_default(1, 2)
# print(result)

def func_sum_values_with_names(a, b=3, c=10):
    res = (a + b) / c
    return res


# result = func_sum_values_with_names(c=5, a=5, b=2)
# print(result)

def func_sum_values_with_types(a: float, b: float, c=10.0) -> float:
    res = (a + b) / c
    return res


# result = func_sum_values_with_types(c=5, a=5, b=2)
# print(result)

# input, str, abs, char, ord, encode, decode, open (with)

# side = float(input("Введите первую сторону квадрата: "))
# print(side ** 2)

# val1 = 123.2
# print(type(val1))
# val1 = str(val1)
# print(type(val1))

print(ord("A"))
print(chr(66))

print("Python".encode())

str1 = b'\x01'
print(str1.decode())


file = open("temp2/new.txt", mode="w", encoding="utf-8")
file.write("123124")
file.close()

with open("temp2/new.txt", mode="w", encoding="utf-8") as file:  # alias - псевдоним
    file.write("123124")
    # файл всё ещё открыт

# файл закрыт -> file.close()
