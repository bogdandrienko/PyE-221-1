values = [1, False, 2, "Python", 3]


# for value in values:
#     index = values.index(value)  # берёт первое совпадение!!! если значения не уникальные нельзя!!!
#     print(index-1, value)

# index = 0  # лишний код и расчёты !
# for value in values:
#     index += 1  # лишний код и расчёты !
#     print(index-1, value)

# for index in range(0, len(values)):
#     value = values[index]  # лишний код и расчёты !
#     print(index, value)

# for count, value in enumerate(values):  # map filter (itertools)
#     print(count, value)

# while - бесконечность
# for - временная сложность
# for i in range(1, 100):
#     for j in range(1, 100):
#         for k in range(1, 100):
#             print("")


# map, filter

# map - функция высшего порядка (принимает функцию как аргумент), которая выполняет на массиве ряд одних и тех же операций

def double(val: float) -> float:
    return val ** 2


list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:
    result = double(val=i)
    list2.append(result)
print(list2)  # [1, 4, 9, 16, 25]

list3 = [double(val=i) for i in list1]
print(list3)

# прогрев (кэширование) функций

list4 = list(map(double, list1))
print(list4)

# class Map1:
#     def __list__(self):
#         pass

list5 = list(map(lambda y: y ** 2 + 1, list1))
print(list5)

# filter - возвращает новый массив (отфильтрованный), функция которого возвращает True

list6 = list(filter(lambda x: x % 2 != 0, list1))
print(list6)

arr1 = ["Python", "Bogdan", "Teach", "Purum"]
list7 = list(filter(lambda x: "P" in x, arr1))
# list7 = list(filter(lambda x: str(x).find("P") <= -1, arr1))
print(list7)
list8 = []
for i in arr1:
    if "P" in i:
        list8.append(i)
    # else:
    #     continue
print(list8)  # ['Python', 'Purum']
