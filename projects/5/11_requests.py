import time

import requests  # - библиотека для формирования HTTP - запроса

# грузить картинки
# отправлять запросы
# получать ответ
# парсить данные

# HTTP  - GET POST PUT(PUTCH) DELETE (CRUD)

# response = requests.get(url="https://jsonplaceholder.typicode.com/todos/1")
# print(response)  # 200 - OK - успешный ответ https://developer.mozilla.org/ru/docs/Web/HTTP/Status
# print(type(response))
# print(response.json())
# print(type(response.json()))

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# response = requests.get(url="https://openweathermap.org/city/1526384", headers=headers)
# print(response.text)
#
# with open('new.html', mode='wb') as file:
#     file.write(response.content)

while True:
    url = 'https://picsum.photos/300/300/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers, timeout=10)
    with open('new.jpg', mode='wb') as file:
        file.write(response.content)

    time.sleep(0.1)
