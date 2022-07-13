import time


def decorator_before(func):  # ссылка на функцию
    def with_before():
        print('start decorator')

        #
        # ядро функции
        func()  # вызов функции
        # ядро функции
        #

        print('end decorator!')

    return with_before


@decorator_before
def write():
    #
    # ядро функции
    print("Write file!")
    # ядро функции
    #


@decorator_before
def read():
    print('start action!')

    #
    # ядро функции
    print("Read file!")
    # ядро функции
    #

    print('Completed!')


# write()


# read()

def decorator_measure_time(function):
    def decorator(*args, **kwargs):  # args - позиционные - tuple(1,2,3,4) | kwargs - {"key_1": 12, "key_2": 13}
        time_start = time.perf_counter()
        result = function(*args, **kwargs)
        print(time.perf_counter() - time_start)
        return result

    return decorator


@decorator_measure_time
def tick(value: float):
    print('start tick')
    time.sleep(value)
    print('end tick')

    return f'completed of {value}'


# result1 = tick(1.5, 2.6)
# print(result1)
# result2 = tick(**{"value": 1.5})
result2 = tick(value=1.6)
# print(result2)

val1 = [12, [12, True, "15"], "15"]


# val1 = [12, "13", 15]
# print(12, True, 15)


# print(type(*val1))


def get_list(a, b, c):
    print(a)
    print(b)
    print(c)
    return a, b, c


# res = get_list(*val1)

val2 = {"title": "Алиса", "surname": "12"}


# print(*val2)


def get_list1(surname: str, title):
    print(f'title: {title}')
    print(f'surname: {surname}')


get_list1(**val2)
