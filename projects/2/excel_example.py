import os
import openpyxl
from openpyxl.utils import get_column_letter

dir_name = 'dist'
files = []

# читаем все файлы из заданной директории(папки), только xlsx
for filename in os.listdir(dir_name):  # os.listdir - принимает в себя директорию откуда нужно вывести все имена файлов
    # print(filename.upper())  # делает все буквы заглавными
    # print(filename.lower())  # делает все буквы прописными
    # print(filename.capitalize())  # делает все буквы как в предложении(первая заглавная, остальные маленькие)
    # print(filename.strip())  # очищает пробелы, табуляции и знаки переноса со строки по краям

    filename1 = filename.split(sep='.')  # метод для строки, который режет её по сепаратору(набор символов)
    # print(filename)
    # print(type(filename))
    # print(filename1)
    # print(type(filename1))

    if filename1[-1] == 'xlsx' or filename1[-1] == 'xls':  # учли, что формат файла может быть устаревшим
        files.append(filename)
    else:
        pass
print(files)

data = []

for file in files:  # проходим циклом по массиву с нужными именами файлов

    # конкатенация строк или сложение строк
    file_name1 = dir_name + '/' + file
    print(file_name1)

    workbook = openpyxl.load_workbook(file_name1)  # принимает имя файла и открывает его как рабочую книгу
    worksheet = workbook.active
    max_row = worksheet.max_row
    print(max_row)
    max_column = worksheet.max_column + 1
    print(max_column)

    dict1 = {}  # создаём пустой словарь(тип данных ключ-значение)

    city = file.split('.')[-2].split(' ')[-1]
    print(f"Имя файла: {city}")
    if city.isdigit():
        # пропустить итерацию цикла
        continue


    print("")
    dict1["Город"] = city
    data.append(dict1)

    #############################################################

    # тут будет логика обработки excel

    #############################################################

    # worksheet[f'{col}{row}'] = str(name)
print(data)

file_name = "temp/sample_example.xlsx"

# workbook = openpyxl.load_workbook(file_name)
# worksheet = workbook.active
# max_row = worksheet.max_row + 1
# print(max_row)
# print(type(max_row))
# max_column = worksheet.max_column + 1
# print(max_column)
# print(type(max_column))

# with open(os.path.join("dist", filename), 'r') as f:
# text = f.read()
# print(text)

# var_range = range(1, 26)
#
# stroka_2 = []
# stroka2 = ""
# for j in var_range:
#     stroka2 = f"A_{j}"
#     stroka_2.append(stroka2)
# print(stroka_2)
