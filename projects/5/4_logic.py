#  if else, elif,  / switch case

# GO TO
val1 = 4

if val1 > 5:
    print("Правда")

if val1 >= 5:
    print("Правда")
else:
    print("Ложь")

if val1 >= 5:
    print("Правда")
elif val1 >= 0:
    print("Ложь")
else:
    print("Число отрицательное!")

fruit = "абрикос"

if fruit == "абрикос":
    print("У Вас аллергия, будьте осторожны")
elif fruit == "банан":
    print("Всё в норме")
else:
    print("Неизвестный фрукт")

# if fruit == "абрикос":
#     print("У Вас аллергия, будьте осторожны")
# else:
#     if fruit == "банан":
#         print("Всё в норме")
#     else:
#         print("Неизвестный фрукт")

match fruit:
    case "абрикос":
        print("У Вас аллергия, будьте осторожны")
    case "банан":
        print("Всё в норме")
    case _:
        print("Неизвестный фрукт")
