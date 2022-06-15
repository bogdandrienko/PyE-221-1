import requests
import json

var_dict1 = dict(Age=24, Name='Ally')  # создание словаря
print(var_dict1)

var_dict2 = {"Age": 24, "Name": 'Ally'}  # создание словаря
print(var_dict2)

var_dict3 = {}  # создание словаря
var_dict3["Age"] = 24
var_dict3["Name"] = 'Ally'
print(var_dict3)

var_dict4 = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": {
        "streetAddress": "Московское ш., 101, кв.101",
        "city": "Ленинград",
        "postalCode": 101101
    },
    "phoneNumbers": [
        "812 123-1234",
        "916 123-4567"
    ]
}
print(type(var_dict4))


print("\n\n\n\n\n")

url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)  # Объект библиотеки
json_data = response.content.decode()  # строка
print(json_data)

with open('data.json', 'w') as file:
    json.dump(json_data, file)
    # json.dumps()

# with open('src/dist/new_file.json', 'r') as file:
#     json_data1 = json.loads(file.read())
#     print(json_data1)
#     json.load()
#     json.loads()


url = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url)  # Объект библиотеки
# response.status_code  # 200
# response.content  # [...]
print(response.content.decode())
print(type(response.content.decode()))
json_data1 = json.loads(response.content.decode())
print(json_data1[7])
print(type(json_data1[7]))

for i in json_data1:
    print(i["title"])
    with open(f'hello/data_{i["id"]}_new_new.json', 'w') as file:
        json.dump(json_data, file)
