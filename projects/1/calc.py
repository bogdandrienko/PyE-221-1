import math


def calc(number1, number2, operation="-"):
    # print(number1, number2, operation)
    if operation == "+":
        return number1 + number2
    if operation == "-":
        return number1 - number2
    if operation == "*":
        return number1 * number2
    if operation == "/":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 / number2
    if operation == "**":
        return number1 ** number2
    if operation == "//":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 // number2
    if operation == "sqrt":
        return math.sqrt(number1)
    if operation == "%":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 % number2


# pass - пропуск строки

# num1 = int(input("Введите первое число:"))
# num2 = int(input("Введите второе число:"))
# oper = str(input("Введите операцию:"))
# result = calc(num1, num2, oper)
result = calc(10, 20)
print(result)

result1 = calc(operation="/", number1=10, number2=2)
print(result1)


def calc_3(number1, number2, operation="-"):
    # print(number1, number2, operation)
    if operation == "+":
        return number1 + number2
    if operation == "-":
        return number1 - number2
    if operation == "*":
        return number1 * number2
    if operation == "/":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 / number2
    if operation == "**":
        return number1 ** number2
    if operation == "//":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 // number2
    if operation == "sqrt":
        return math.sqrt(number1)
    if operation == "%":
        if number2 == 0:
            print("Второе число не может быть 0")
        else:
            return number1 % number2
