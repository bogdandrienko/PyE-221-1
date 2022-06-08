import datetime as dt
from datetime import date
from datetime import time
from datetime import datetime


today = dt.datetime.now()  # текущую дату и время
print(today)
print(type(today))
# print("Date :", today)

# print(str(today).split(' ')[1][0:8])  # получение времени из .now() и последующая обрезка

new_today = today.strftime("%d-%m-%Y %H:%M.%f     %a %A   %d  %b %B ")  # полный вид строки (формат даты) для Азии
print(new_today)

# https://docs-python.ru/standart-library/modul-datetime-python/kody-formatirovanija-strftime-strptime-modulja-datetime/

# today_date = date.today()
# print(today_date)


today_hour = dt.datetime.now().strftime("%H")  # получаем только часы
print(today_hour)

# Timestamp = 1  # целочисленное выражение текущей секунды
# date_From_Timestamp = datetime.fromtimestamp(Timestamp)  # превращение числа в тип данных даты (1970-01-01 06:00:00)
# print(date_From_Timestamp)
