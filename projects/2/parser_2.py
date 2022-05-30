import json
import requests


# url = "https://api.instantwebtools.net/v1/airlines/4"
# response = requests.get(url)
# json_data = response.content.decode()
# print(json_data)


url = "https://jsonplaceholder.typicode.com/posts"
# url = "https://api.instantwebtools.net/v1/airlines"
response = requests.get(url)
content = response.content
print(type(content))
json_data = content.decode()
print(type(json_data))
# print(json_data)
airlines = json.loads(json_data)
print(type(airlines))
print(airlines[0:2])
# print(type(json.load(json_data)))

for airline in airlines:
    # менеджер контекста
    with open(f'temp/data_{airline["id"]}.json', 'w') as file:
        json.dump(airline, file)


# with open('data.json', 'w') as file:
#     json.dump(json_data, file)
    # json.dumps()

# with open('src/dist/new_file.json', 'r') as file:
#     json_data1 = json.loads(file.read())
#     print(json_data1)
#     json.load()
#     json.loads()