import openpyxl

# чтение
# обрабатываем данные
# записываем в исходный файл (можно исходный файл удалять)


workbook = openpyxl.load_workbook("""temp/sample_example.xlsx""")

# берём активную страницу из рабочей книги
worksheet = workbook.active

# берём последнюю строку в excel-файле
max_row = worksheet.max_row + 1
print(max_row)
print(type(max_row))
# берём последнюю колонку в excel-файле
max_column = worksheet.max_column + 1
print(max_column)
print(type(max_column))


for row in range(1, max_row):
    for col in range(1, max_column):
        value = worksheet.cell(row=i, column=j).value
