x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b + 10

print(x(5, 7))


def ex_lambda1(a, b):
    value = a * b + 10
    return value


print(ex_lambda1(5, 7))


def ex_lambda2(a, b):
    return a * b + 10


print(ex_lambda2(5, 7))


def ex_lambda3(a, b): return a * b + 10


print(ex_lambda3(5, 7))

lst = [('candy', '30,30', '100'), ('apple', '10', '200'), ('baby', '20', '300')]
lst.sort(key=lambda y: y[1])

# list2 = []
# for x in lst:
#     a, b, c = x
#     print(f"a: {a}")
#     print(f"b: {b}")
#     print(f"c: {c}")
#     list2.append(b)
# print(lst)
#
# print(list2)
# list2.sort()
# print(list2)

print('\n\n\n\n\n**********\n\n\n\n\n')

dict1 = [
    {'Name': 'A', 'age': 26, 'quality': 1},
    {'Name': "B", 'age': 20, 'quality': 2},
    {'Name': "C", 'age': 33, 'quality': 3}
]
print(dict1)
dict1.sort(key=lambda y: y["age"], reverse=True)
print(dict1)
