def is_balanced(string: str):
    if not string or len(string) & 1:
        return False

    open_s = "({["
    closed_s = ")}]"
    stack = []

    for char in string:
        if char in open_s:
            stack.append(char)  # Если текущий символ является открывающей скобкой поместите его в массив
        if char in closed_s:
            if not stack:
                return False  # Если символа нет, то нет баланса
            top = stack.pop()  # Если текущий символ является закрывающей скобкой извлечь его из массива
            if (top == '(' and char != ')') or (top == '{' and char != '}' or (top == '[' and char != ']')):
                return False  # Если символ "зеркально" не совпадает, то нет баланса
    return not stack  # Если массив пустой, то есть баланс


if __name__ == '__main__':
    string1 = '{}()[]'  # balanced
    string2 = '{()}[{}]'  # balanced
    string3 = '{[{}{}]}[()]'  # balanced
    string4 = '{(})'  # not balanced
    string5 = '{}('  # not balanced
    print('balanced' if is_balanced(string=string1) else 'not balanced')

    # todo second intersection array
    # Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
    # Надо вернуть [1, 2, 2, 3] (порядок неважен)
