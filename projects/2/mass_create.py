var_list = ["Almaty", "Nur-Sultan", "Taraz", "Ekibastuz"]
num_list = range(1, 50)

# создание одиночного файла
with open(file="new/new.txt", mode="a", encoding="cp1251") as file:
    file.write(var_list[2])

# создание множества файлов
for num in num_list:
    with open(file=f"new/new_{num}.txt", mode="w", encoding="cp1251") as file:
        file.write(var_list[3] + "_" + str(num))
