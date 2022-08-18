# try:
#     print("открываем файл и загружаем в память")  # открытие базы данных, открытие транзакции
#     print(10 / 0)
#
#     print("Читаем файл")
# except Exception as error:
#     print(error)
#     print("закрываем файл и выгружаем из памяти")

# finally, else, вызов исключения, собственные исключения


# try:
#     print("пытаемся перевести деньги коллеге")  # открытие базы данных, открытие транзакции
#     print("списание суммы с нашего счёта")
#     print(10 / 0)  # код, который может вызвать, а может и не вызвать ошибку
# # except ZeroDivisionError:  # ZeroDivisionError(ArifmeticError) ArifmeticError(Exception)
# #     print(f"Ваша сумма ниже лимита!")
#     print('успешное закрытие транзакции')
# except BufferError:
#     print(f"Недоступное действие")
#     print('отмена транзакции')
# except Exception as error:
#     if error == "division by zero":
#         print(f"Ваша сумма ниже лимита!")
#     print(f"error: {error}")
#     print("пополнение счёта коллеги")
#     print('отмена транзакции')
# else:
#     print('успешное закрытие транзакции')
# finally:
#     print("тут код, который выполняется всегда!")
#     print('вывод данных о счёте')

def sum2(a, b):
    result = a + b
    if result <= 0:
        raise ArithmeticError
    return result


# res = sum2(2, -2)
# print(res)

# FileExistsError - попытка создания файла или директории, которая уже существует.
# FileNotFoundError - файл или директория не существует.

text = "Hello world!"
try:
    file = open("temp2/new.txt", mode="w", encoding="utf-8")
    file.write(text)
except FileNotFoundError as error:
    print(f"Директории не существует! {error}")

    import os
    os.mkdir("temp2")

finally:
    # file.close()
    pass
