import requests
import json


url = 'https://jsonplaceholder.typicode.com/posts/1'
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url=url, headers=headers)

print(response)
print(type(response))

print(response.status_code)
print(response.content)

json_data = json.loads(response.content)  # bytes -> json(dictionary)

print(json_data)
print(type(json_data))

file = open('new.json', 'w')
json_string = json.dumps(json_data)
file.write(json_string)
file.close()

print('\n\n\n\n\n\n*************\n\n\n\n\n\n')

urls = 'https://jsonplaceholder.typicode.com/posts'
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url=urls, headers=headers)

print(response.content)
print(type(response.content))

json_data = json.loads(response.content)  # bytes -> json(dictionary)

print(json_data)
print(type(json_data))

index = 0
for i in json_data:
    index = index + 1
    with open(f'new/new_{index}.json', 'w') as file:
        json_string = json.dumps(i)
        file.write(json_string)
