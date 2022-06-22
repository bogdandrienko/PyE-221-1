import datetime


list1 = [1, 2, 3, 5, 7, "123"]
print(list1)
print(type(list1))

set1 = set(list1)  # несортированный массив с уникальными значениями
set2 = {1, 2, 3, 5, 7, "123"}
print(set1)
print(type(set1))

set1.add(1111111)  # добавление элемента
print(set1)

print("\n\n\n\n\n************\n\n\n\n\n")


set3 = set(list1)
set3.add("2222222222")
print(set3)
set4 = set(list1)
set4.add("333333333333")
print(set4)

set5 = set3.difference(set4)  # разница
print(set5)

set6 = set3.intersection(set4)  # пересечения (совпадения)
print(set6)

set7 = set3.union(set4)  # сложение двух множеств
print(set7)

set8 = set(list1)
set8.add(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
print(type(datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
print(set8)
set8.remove(5)  # удаление элемента
print(set8)

val1 = [x for x in set8 if isinstance(x, str)]  # генератор (list compehansions)
val2 = []
for x in set8:
    if isinstance(x, str):
        val2.append(x)
    else:
        pass
print(val1)
print(val2)

set6 = {1, 2, [3, 2, 6], 5, {"key_1": 1}, {1, 2, 3, 5, 7, "123"}}
set7 = {1, 2, [3, 2, 6, 10], 5, {"key_1": 1}, {1, 2, 3, 5, 7, "123"}}
set8 = {1, 2, [3, 2, 6], [3, 2, 6, 10], 5, {"key_1": 1}, {1, 2, 3, 5, 7, "123"}}
