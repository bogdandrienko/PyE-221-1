import time
import json
import requests  # - библиотека для формирования HTTP - запроса

# грузить картинки
# отправлять запросы
# получать ответ
# парсить данные

# HTTP  - GET POST PUT(PUTCH) DELETE (CRUD)

# response = requests.get(url="https://jsonplaceholder.typicode.com/todos/1")  # фейковая api
# print(response)  # 200 - OK - успешный ответ https://developer.mozilla.org/ru/docs/Web/HTTP/Status
# print(type(response))
# # print(response.json())
# # print(type(response.json()))
# print(response.content)
# print(type(response.content))

# сериализация / десериализация

# with open('new.json', mode='r') as file:
#     dictionary1 = json.load(file)  # позволяет сериализовать файловый - объект в словарь
#     print(dictionary1)
#     print(type(dictionary1))

# response = requests.get(url="https://jsonplaceholder.typicode.com/todos/1")
# print(response.content)
# print(type(response.content))
# dictionary2 = json.loads(response.content)  # позволяет сериализовать строку или байтовую строку в словарь
# print(dictionary2)
# print(type(dictionary2))

# with open('new1.json', mode='w') as file:
#     dict3 = {
#         "userId": 1,
#         "id": 1,
#         "title": "delectus aut autem",
#         "completed": [
#             {
#                 "userId": 1,
#                 "id": 1,
#                 "title": "delectus aut autem",
#                 "completed": False
#             },
#             {
#                 "userId": 1,
#                 "id": 1,
#                 "title": "delectus aut autem",
#                 "completed": False
#             },
#             {
#                 "userId": 1,
#                 "id": 1,
#                 "title": "delectus aut autem",
#                 "completed": False
#             }
#         ]
#     }
#     # json.dump(dict3, file)  # позволяет записать объект JSON в файл
#     ret = json.dumps(dict3)  # сериализует объект JSON в строку, которую можно без потерь записать в файл
#     print(ret)
#     print(type(ret))
#     file.write(ret)

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# response = requests.get(url="https://openweathermap.org/city/1526384", headers=headers)
# print(response.text)
#
# with open('new.html', mode='wb') as file:
#     file.write(response.content)

# while True:
#     url = 'https://picsum.photos/300/300/'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/102.0.0.0 Safari/537.36'
#     }
#     response = requests.get(url=url, headers=headers, timeout=10)
#     with open('new.jpg', mode='wb') as file:
#         file.write(response.content)
#
#     time.sleep(0.1)

# c = lambda a, b: a + b
# print(c(12, 15))

# response = requests.get(url="https://jsonplaceholder.typicode.com/todos").json()
# print(response)
# list1 = [x.get("title", None) for x in response if x.get("id", None) % 2 == 0]
# print(list1)

# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/102.0.0.0 Safari/537.36'
#     }
# response = requests.get(url="https://www.gismeteo.kz/weather-shymkent-5324/", headers=headers)
# # print(response.text)
# new_data = response.text.split(sep='<div class="weathertabs day-1">')[1]
# # print(new_data)
# new_data2 = new_data.split(sep='tab-temp')[1].split(sep='tab-image')[0]
# # print(new_data2)
# new_data3 = new_data2.split(sep='<span class="unit unit_temperature_c">')
# # print(new_data3)
# night = new_data3[1].split(sep='<')[0]
# day = new_data3[2].split(sep='<')[0]
# print(f"day: {day} | night: {night}")


