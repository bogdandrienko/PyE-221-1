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


write()


# read()


class App:
    def __init__(self):
        pass

    @staticmethod
    def func1():
        pass


App.func1()
