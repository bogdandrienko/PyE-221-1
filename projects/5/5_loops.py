#          0  1  2  3  4
value_8 = [1, 4, 6, 8, 9]  # tuple, set

for i in value_8:
    if i < 7:
        # continue
        break
    else:
        print(i*i)
value7 = {
    "key_1": "value_1",
    "key_2": 10,
    "key_3": True
}

for key, value in value7.items():  # (key, value) #
    print(f"{key}:  {value} type - {type(value)}")

index = 0
while index < 100:
    index += 1
    if index % 2 != 0:
        continue
    print(index)
    # if index == 88:
    #     break


#       0 1 2          -2 -1
str6 = "Pythoon is awesome!"
print(str6)
print(str6[2])
print(str6[-2])
val1 = len(str6.split(' ')[0])
print(f"val1: {val1}")
print(str6[val1:].strip())

#        [start, stop, step]
print(str6[0:len(str6):2])

list2 = [{f"тема {i}": 100 - i, f"текст {i}": i} for i in range(1, 100) if i <= 30]
print(len(list2), list2)
print(len(list2[:10]), list2[:10])
print(len(list2[:-11:-1]), list2[:-11:-1])

page = 2  # выбранная страница
limit = 10  # по 10 комментариев на страницу
# [1......30] - долго и дорого
# [[1...10], [11..20], [21...30]] - оптимизация
# print(str6.split(" "))
#
# arr1 = ['Python', 'is', 'awesome!', 'is', 'awesome!']
# str2 = ", ".join(arr1)
# print(str2)