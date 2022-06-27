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

print('\n\n\n\n\n**********\n\n\n\n\n')

list5 = [1, 2, 5, 10, 4, 2]
print(list5)
list5.sort(reverse=True)
print(list5)

str1 = "ABCDfff124124wecerwfgyhtyjsafs"
print(str1)
arr1 = []
for x in str1:
    arr1.append(x)
print(arr1)
arr2 = [x for x in str1]  # list comprehansions
print(arr2)
arr2.sort(reverse=False)
print(arr2)
str3 = ''
for x in arr2:
    str3 += x
print(str3)
# print(str1)
str4 = "".join(arr2)
print(str4)

print('\n\n\n\n\n**********\n\n\n\n\n')

arr6 = [x for x in "ABCDfff124124wecerwfgyhtyjsafs"]
arr6.sort(reverse=True)
arr8 = "".join(arr6)
print(arr8)

print('\n\n\n\n\n**********\n\n\n\n\n')

text1 = 'Идейные соображения высшего порядка, а также сложившаяся структура организации представляет собой интересный' \
        ' экспCтруктураеримент проверки форм развития. '

substring = 'структура'
find1 = text1.find(substring)
print(find1)
print(text1[find1:find1+len(substring):1])

