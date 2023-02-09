class LifoObject(object):
    """
    LIFO (Last In, First Out – «последним пришёл — первым ушёл»
    """

    # store: list[any] = ["no valid"]  # атрибут класса

    def __init__(self):
        self.__store: list[any] = []  # атрибут экземпляра класса

    # stack
    def setter(self, new_tarelka: any):  # push
        self.__store.append(new_tarelka)

    def getter(self) -> any:  # pop
        if len(self.__store) < 1:
            return None
        elem = self.__store[-1]
        del self.__store[-1]
        return elem

    def print_all(self):
        print(self.__store)


class FifoObject(object):
    """
    FIFO (First In, First Out – «первым пришёл — первым ушёл»
    """

    # store: list[any] = ["no valid"]  # атрибут класса

    def __init__(self):
        self.__store: list[any] = []  # атрибут экземпляра класса

    # stack
    def setter(self, new_tarelka: any):  # push
        self.__store.append(new_tarelka)

    def getter(self) -> any:  # pop
        if len(self.__store) < 1:
            return None
        elem = self.__store[0]
        del self.__store[0]
        return elem

    def print_all(self):
        print(self.__store)

# stack1 = LifoObject()
# stack1.setter("Tarelka 1")  # ложим следующую (первую)
# stack1.setter("Tarelka 2")  # ложим следующую (вторую)
# stack1.setter("Tarelka 3")  # ложим следующую (третью)
# print(stack1.getter())  # извлекает последнюю(третью)
# stack1.setter("Tarelka 4")  # ложим следующую (3-4)
# stack1.print_all()
# print(stack1.getter())  # извлекает последнюю("Tarelka 4")
# print(stack1.getter())  # извлекает последнюю(третью)
# print(stack1.getter())  # извлекает последнюю(третью)
# print(stack1.getter())  # извлекает последнюю(третью)
# stack1.print_all()


stack2 = FifoObject()
stack2.setter("Tarelka 1")  # ложим следующую (первую)
stack2.setter("Tarelka 2")  # ложим следующую (первую)
stack2.setter("Tarelka 3")  # ложим следующую (первую)
print(stack2.getter())      # извлекает первую("Tarelka 1")
stack2.setter("Tarelka 4")  # ложим следующую (3-4)
print(stack2.getter())      # извлекает последнюю(третью)
