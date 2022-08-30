# class Meter():
#     def __init__(self, dev):
#         self.dev = dev
#     def __enter__(self):
#         #ttysetattr etc goes here before opening and returning the file object
#         self.fd = open(self.dev, MODE)
#         return self
#     def __exit__(self, type, value, traceback):
#         #Exception handling here
#         close(self.fd)
#
# meter = Meter('dev/tty0')
# with meter as m:
#     #here you work with the file object.
#     m.fd.read()
import datetime


# Процедурное программирование               Паскаль
# Функциональное программирование            F#
# Объектно-ориентированное программирование  C#, Делфи, Python, c++


#                     объект - видимость, рендеринг, коллизии (физики)
#                     техника - скорость, масса, может с ними взаимодействовать
#         сухопутные             водоплавающие  - точки, где можно перемещаться
#  Велосипед Машина Мотоцикл  гидроскутер  Лодка     - текстуры, цвет


# print(type(10))
# print(type(True))
# print(type([True, 12]))

class Obj:
    is_start_rendering1 = True
    visible = False  # публичное свойство экземпляра класса
    _visible = True  # защищённое свойство экземпляра класса
    __visible = True  # приватное свойство экземпляра класса

    def __init__(self, mass=10.0, is_start_rendering=True):  # магический метод(функция)
        self.mass = mass
        self.is_start_rendering1 = True
        self.is_start_rendering = is_start_rendering
        self.mass2 = 12
        self.__mass3 = 12

    def get_visibility(self) -> bool:  # метод
        """
        Return state of is visibile obj
        :return: bool
        """
        return self._visible

    def set_visibility(self, is_checked: bool) -> None:
        self._visible = is_checked
        print(self.mass2)

    def get_mass(self):
        return self.mass

    # def switch_visibility(self) -> None:  # метод
    #     """
    #     Этот метод должен переключать видимость
    #     :return: None
    #     """
    #     self._visible = not self._visible

    # def switch_and_return_visibility(self) -> bool:  # метод
    #     """
    #     Этот метод должен переключать видимость
    #     :return: None
    #     """
    #     self._visible = not self._visible
    #     return self._visible

    # def print_visibility(self) -> None:
    #     print(self._visible)


class Vehicle(Obj):
    def __init__(self, speed: float):
        super().__init__(mass=100)
        self.speed = speed
        self.mass = 200

    def get_parent_mass(self):
        return super().get_mass()

    # как получить значение такого атрибута, но от родителя
    # использование  public || private || protected
    # множественное наследование и "проблема ромба"
    # бинарное дерево


class Some:
    pass


som1 = Some()

veh1 = Vehicle(speed=50.2)
print(veh1.mass)
print(veh1.get_parent_mass())


#
# print(Obj.visible)
# print(Obj._visible)
# # print(Obj.__visible)
#
# new_obj_1 = Obj()  # создание экземпляра
# print(new_obj_1)
# print(new_obj_1.visible)
# print(new_obj_1._visible)
# # print(new_obj_1.__visible)
# print(type(new_obj_1))

# new_obj_1 = Obj()
#
# print(new_obj_1.get_visibility())
#
# # new_obj_1.switch_visibility()
#
# print(new_obj_1.get_visibility())
#
# new_obj_1.set_visibility(is_checked=not new_obj_1.get_visibility())
#
# print(new_obj_1.get_visibility())


class Parall:
    def __init__(self, side1: int, side2: int):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side1 / 3 * side2

    def check_is_square(self) -> bool:
        # if self.side1 == self.side2:
        #     return True
        # else:
        #     return False
        return self.side1 == self.side2

    def get_perimeter(self) -> int:
        return (self.side1 + self.side2) * 2

    def get_square(self) -> int:
        if self.check_is_square():
            return self.side1 ** 2  # квадрат
        else:
            return self.side1 * self.side2  # многоугольник

    def __add__(self, other) -> int:  # +
        if isinstance(other, Parall):
            return self.get_perimeter() + other.get_perimeter()
        else:
            raise TypeError

    def sum_self(self, other) -> int:  # +
        if isinstance(other, Parall):
            return self.get_perimeter() * other.get_perimeter()
        else:
            raise TypeError


parall1 = Parall(side1=2, side2=3)
parall2 = Parall(side1=30, side2=30)
parall3 = Parall(side1=50, side2=30)


# print(parall1 + 10)

# list1 = [Parall(side1=x + 1, side2=x + 2) for x in range(1, 101)]
# sum1 = 0
# print(list1)
# for i in list1:
#     sum1 += i.get_square()
# print(sum1)
# print(parall1.get_perimeter())

# if parall1.check_is_square():
#     print('Это квадрат!')
# else:
#     print('Это прямоугольник!')
#
# if parall2.check_is_square():
#     print('Это квадрат!')
# else:
#     print('Это прямоугольник!')


class HelpPython:
    class Time:
        @staticmethod
        def get_current_time(timezone: int, formatting="23:59:59"):
            import datetime
            datetime = datetime.datetime.now()

            match formatting:
                case "23:59:59":
                    return datetime.strftime('%H:%M:%S')
                case "23:59:59.999":
                    return datetime.strftime('%H:%M:%S ...')
                case "23:59":
                    return datetime.strftime('%H:%M')
                case _:
                    return datetime

        @staticmethod
        def get_different_times_in_seconds(datetime1: datetime.datetime, datetime2: datetime.datetime) -> int:
            # datetime1 - datetime2
            return 0

    class Variable:
        class Types:
            @staticmethod
            def example():
                value1 = 10  # - 100
                value2 = 10.0  # -10.6
                value3 = True  # False
                value4 = ""
                value5 = "10"
                value6 = "Hello"
                str1 = b'\x01\x02\x03\x04\x05'
                str2 = "\n \t  I'am "
                str3 = """\n \t  I'am """
                str4 = '''\n \t  I'am '''
                str5 = '\n \t \\ I\'am '
                str6 = r"\n\tC:\Users\bogdan\Desktop\Django\Курс лекций Django1\Python"

        @staticmethod
        def convert_to_string(value) -> str:
            # return str(value)
            # return str(value).format(1)
            return f"{value}"

        @staticmethod
        def get_type_variable(var) -> type:
            return type(var)

        @staticmethod
        def get_value_from_dict(dictionary: dict, value: str, default_value, is_logging=False):
            try:
                # return dictionary.get("username", None)  # не вызывает исключения при отсутвии ключа
                return dictionary[value]
            except Exception as error:
                if is_logging:
                    print(f"Ошибка: {error}")
                return default_value

    class Arifmetic:
        @staticmethod
        def example():
            import math  # много математики

            val1 = -10
            val2 = 15

            result = math.sqrt(16)  # int(math.sqrt(16))
            print(type(result > 3.9))

            print(result > 3.9)

            abs(val1)

            print(10 * 4)
            print(10 ** 4)
            print(10 / 5)
            print(10 // 5)  # int(10 / 5) round(10 / 3, 2) 3.33

            print(16 ** 0.5)

            print(7 % 2)  # 1
            print(6 % 2 == 0)  # чётное

    class ExceptionHelps:
        class MyException1(Exception):
            def __init__(self, exception_text: str, sector: str, level_error: int, critical: bool):
                self.exception_text = exception_text
                self.datetime = datetime.datetime.now()
                self.sector = sector
                self.level_error = level_error
                self.critical = critical

            def print_error(self):
                print(f"{self.sector}: {self.exception_text} {self.datetime}")


dict1 = {"name": "Python"}
print(HelpPython.Variable.get_value_from_dict(dictionary=dict1, value="name", default_value="C++", is_logging=False))


class MyException(Exception):
    def __init__(self, exception_text: str, sector: str, level_error: int, critical: bool):
        self.exception_text = exception_text
        self.datetime = datetime.datetime.now()
        self.sector = sector
        self.level_error = level_error
        self.critical = critical

    def print_error(self):
        print(f"{self.sector}: {self.exception_text} {self.datetime}")


def test1(a, b):
    try:
        if b == 0:
            raise HelpPython.ExceptionHelps.MyException1(exception_text="кто-то накосячил с кодом",
                                                         sector="test1 Вычислительное ядро",
                                                         level_error=3, critical=False)
        c = a / b
        return c
    except HelpPython.ExceptionHelps.MyException1 as error:
        print(f"MY {error}")
        print(error.sector)
        print(error.print_error())
        return a
    except Exception as error:
        print(f"123124124 {error}")
        return None


print(test1(9, 0))


class BinaryTree:
    def __init__(self, data: int):
        self.left = None
        self.right = None
        self.root = data

    def get_data(self):
        return self.root

    def insert_new_data(self, data: int):
        if self.root:
            if data < self.root:

                # левый
                if self.left is not None:
                    self.left.insert_new_data(data)
                else:
                    self.left = BinaryTree(data)
                # левый

            elif data > self.root:

                # правый
                if self.right is not None:
                    self.right.insert_new_data(data)
                else:
                    self.right = BinaryTree(data)
                # правый

            else:
                print('Значение повторяется')

        else:
            self.root = data

    def print_all_edges(self):
        print(self.root)
        print(self.left)
        print(self.right)


tree1 = BinaryTree(1)  # создание экземляра класса - создание объекта
tree1.insert_new_data(2)
tree1.insert_new_data(3)
tree1.insert_new_data(9)
tree1.insert_new_data(6)
tree1.insert_new_data(11)
tree1.insert_new_data(15)
print(f"root: {tree1.root}")
print(f"root: {tree1.right.root}")

print(f"root: {tree1.right.right.root}")

print(f"root: {tree1.right.right.right.root}")

print(f"root: {tree1.right.right.right.right.root}")
print(f"root: {tree1.right.right.right.left.root}")

print(f"root: {tree1.right.right.right.right.right.root}")

# class BinaryTree2:
#     def __init__(self, data: int):
#         self.left = None
#         self.right = None
#         self.root = data
#
#
# tree1 = BinaryTree2(1)  # создание экземляра класса - создание объекта
# tree2 = BinaryTree2(2)  # присвоение в левую ветку нового объекта
# tree1.left = tree2  # присвоение в правую ветку нового объекта
# tree1.right = BinaryTree2(3)  # присвоение в правую ветку нового объекта
# tree1.right.right = BinaryTree2(6)
# print(tree1)
# print(f"root: {tree1.root}")
# print(f"root: {tree1.left.root}")

index = 0
def substr(val: int):
    global index
    index += 1
    print(f'вход номер {index}, значение {val}')

    if val == 1:
        return val
    else:
        return substr(val//2)

print(substr(12))

# CreateReadUpdateDelete
# CRUD

# Date and time is: 2021-07-03 16:21:12.357246
# Timestamp is: 1625309472.357246
