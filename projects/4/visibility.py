value = len("12")  # built-in Python
value1 = abs(-10)
# abs = 10

# print(local_var)
local_var = 12  # глобальная область видимости
print(local_var)


# __main__ local_var -> func1 global local_var -> func2(local_var)

def func1(local_var):
    # global local_var  # использование переменной из глобальной области видимости

    # print(local_var)
    # local_var = 10  # локальная область видимости func1
    print(local_var)

    def func2(local_var):
        # global local_var

        print(local_var)  # локальная область видимости func2
        # local_var = 11
        print(abs)

    func2(local_var)


func1(local_var)

func1(local_var)
print(local_var)


def clear_func(value1, sep):
    # do something
    return "123"


is_commit = False  # можно изменить
COMMIT = False  # можно изменить, но не желательно (IDE подскажет)


def func_1():
    global is_commit
    global COMMIT
    is_commit = True
    COMMIT = True
    # many code
    # ...
    # value1 = 18


print(is_commit)
func_1()
print(is_commit)
