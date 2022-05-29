# var_list1 = [12, 16, 0, -100, "1234", True]  # массив переменных

# цикл, который "итерируется"(пробегается) по массиву объектов и
# берёт каждый цикл этот объект себе в переменную (i)
# for list_element in [12, 16, 0, -100]:
# for i in var_list1:
#     print(
#         "элемент 'списка': ", var_list1.index(i),
#         i, type(i)
#     )

# for i in var_list1:
#     print(
#         "элемент 'списка': ", var_list1.index(i),
#         i, type(i)
#     )
#     # код до цикла
#     for j in var_list1:
#         # код в цикле
#         print(
#             "элемент 'списка': ", var_list1.index(j),
#             j, type(j)
#         )
#     # код после цикла

# var_int1 = 12
# # код до цикла
# while var_int1 < 500:
#     # код в цикле
#     var_int1 = var_int1 + 1
#     print(var_int1)
#     if var_int1 == 500:
#         print('мы дошли до 500')
# # код после цикла
# print('цикл завершён')

var_list = ["Almaty", "Nur-Sultan", "Taraz", "Ekibastuz"]

str_1 = "Almaty"
str_2 = "Taraz"
print(f"{str_1}+{str_2}")
print(str_1 + "+" + str_2)

truth = 10.5
index_i = 1
for i in var_list:
    # print(i + " " + str(var_list.index(i)+1))
    string_city = f"{i} {truth}"  # конкатенация (сложение)
    print(i + str(truth))
    index_i += 1
