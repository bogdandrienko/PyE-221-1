import requests
import openpyexcel
from openpyexcel.utils import get_column_letter


req_data = requests.get("https://reqres.in/api/users/2").json()
email_from_api = req_data["data"]["email"]
fullname_from_api = f'{req_data["data"]["first_name"]} {req_data["data"]["last_name"]}'

params = (
    {"equal": "$email", "insert": "janet.weaver@reqres.in"},
    {"equal": "$fullname", "insert": "Janet Weaver"},
    {"equal": "$fullname1", "insert": "Janet Weaver1"},
    {"equal": "$fullname2", "insert": "Janet Weaver2"},
    {"equal": "$fullname3", "insert": "Janet Weaver3"},
    {"equal": "$fullname4", "insert": "Janet Weaver4"},
    {"equal": "$another", "insert": "TKINTER"},
)


# Union[tuple[dict]]
def analyze(filename, *args):
    workbook = openpyexcel.load_workbook(filename)
    worksheet = workbook.active
    for row in range(1, worksheet.max_row + 1):
        for column in range(1, worksheet.max_column + 1):
            for arg in args:
                try:
                    if str(worksheet[f"{get_column_letter(column)}{row}"].value) == arg["equal"]:
                        worksheet[f"{get_column_letter(column)}{row}"] = arg["insert"]
                except Exception as error:
                    pass

            # if str(worksheet[f"{get_column_letter(column)}{row}"].value) == equal1:  # сравнение
            #     # worksheet.cell(row=row, column=column)  # <Cell>.value "GET"
            #     worksheet[f"{get_column_letter(column)}{row}"] = \
            #         req_data["data"]["email"]  # <Cell>.value "SETTER"
            # elif str(worksheet[f"{get_column_letter(column)}{row}"].value) == equal2:
            #     worksheet[f"{get_column_letter(column)}{row}"] = \
            #         f'{req_data["data"]["first_name"]} {req_data["data"]["last_name"]}'
            #
            # match str(worksheet.cell(row=row, column=column).value):
            #     case "$email":
            #         worksheet.cell(row=row, column=column, value=email_from_api)
            #     case "$fullname":
            #         worksheet.cell(row=row, column=column, value=fullname_from_api)

    workbook.save(filename)
    workbook.close()


analyze("data.xlsx", *params)
