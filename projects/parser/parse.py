import json
import time
import requests

details = []
with open("docs/pagination/6.json", "r") as file_r:
    json_data = json.loads(file_r.read())
    for vacancy in json_data["items"]:
        try:
            req = requests.get(f'https://api.hh.ru/vacancies/{vacancy["id"]}')  # Посылаем запрос к API
            data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
            req.close()
            details.append(data)
            time.sleep(0.01)
        except Exception as error:
            pass

items = {"items": details}
with open("docs/pagination/6_1.json", "w+") as file_w:
    file_w.write(json.dumps(items, ensure_ascii=True))

with open("docs/pagination/6_1.json", "r") as file_r:
    json_data = json.loads(file_r.read())
    for item in json_data["items"]:
        print(item)
        # print(item["description"])
