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

for count, value in enumerate(values):  # map filter (itertools)
    print(count, value)

# while - бесконечность
# for - временная сложность
# for i in range(1, 100):
#     for j in range(1, 100):
#         for k in range(1, 100):
#             print("")




