import requests
import openpyexcel


urls = "https://reqres.in/api/users/2"

req = requests.get(urls)

print(req.json())

req_data = req.json()

email = req_data["data"]["email"]
fullname = f'{req_data["data"]["first_name"]} {req_data["data"]["last_name"]}'

print(email)
print(fullname)

workbook = openpyexcel.load_workbook("data.xlsx")
worksheet = workbook.active
print(worksheet["A1"].value)


print(worksheet.cell(1,1).value)

max_row = worksheet.max_row
max_column = worksheet.max_column



for row in range(1, max_row+1):
    for column in range(1,max_column+1):
        match str(worksheet.cell(row,column).value):
            case "$email":
                worksheet.cell(row=row, column=column, value=email)
            case "$fullname":
                worksheet.cell(row=row, column=column, value=fullname)
            case _:
                pass
        # print(f"{row} {column} {worksheet.cell(row,column).value}")
workbook.save("data.xlsx")
workbook.close()
