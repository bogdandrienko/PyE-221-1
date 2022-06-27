list1 = [1, 2, 5, [3, 2, 6], {"key_1": 1}, {1, 2, 3, 5, 7, "123"}, 5]
tuple1 = (1, 2, 5, [3, 2, 6], {"key_1": 1}, {1, 2, 3, 5, 7, "123"}, 5)
str1 = "Banan"

search1 = list1.index(5)  # поиск индекса в массиве по элементу
print(search1, " : ", list1[search1])
search2 = str1.index('a')
print(search2, " : ", str1[search2])

search3 = list1.index(5, 3, 7)  # поиск индекса в массиве по элементу, с указанием откуда и до куда искать
print(search3, " : ", list1[search3])

search4 = tuple1.index(5, 3, 7)
print(search4, " : ", tuple1[search4])

list2 = [1, 2, 5, 10, 4, 2]
list2.sort()
print(list2)

# str1 = "ABCDfff124124wecerwfgyhtyjsafs"
letter1 = "#"
print(letter1)
print(type(letter1))

sumvol1 = ord(letter1)  # получаем индекс(число) строчного элемента
print(sumvol1)
print(type(sumvol1))

number1 = chr(35)  # получаем элемент(символ) из индекса
print(number1)
print(type(number1))

# reverse sort
# sort and lambda expression

# search in string
