import requests
from bs4 import BeautifulSoup

url = f'https://myfin.by/converter.html'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
response = requests.get(url=url, headers=headers)  # http запрос

soup = BeautifulSoup(response.content, 'html.parser')
data1 = soup.find_all('div', class_='converter-containers converter-containers--tablet-col-2')
print(data1)
print(len(data1))

print('\n\n\n\n********\n\n\n\n')

data2 = data1[0].text.split('converter-container__inputs')
print(data2)
print(len(data2))

# data2 = data1[0].find_all('div', class_='converter-container__item')
# print(data2)
# print(len(data2))
# for i in data2:
#     print(i.text)
