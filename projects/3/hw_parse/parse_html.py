import requests
from bs4 import BeautifulSoup

url = 'https://myfin.by/converter.html'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')

print(soup)
# print(soup.text)

# data = soup.find_all('div', class_="converter-container__item")

data = soup.findAll("input", class_="input_calc form-control form-input-sum bestmb")

print(data)

values = []
for i in data:

    print(i, '\n')

    sep_name_left = 'id="bestmb_'
    sep_name_right = '" inputmode'

    val_name_1 = str(i).split(sep=sep_name_left)[1]
    val_name_2 = val_name_1.split(sep=sep_name_right)[0]

    print(val_name_2, '\n')

    sep_value_left = 'value="'
    sep_value_right = '"/>'

    val_value_1 = str(i).split(sep=sep_value_left)[1]
    val_value_2 = val_value_1.split(sep=sep_value_right)[0]

    print(val_value_2, '\n')

    dict_value = {
        "name": val_name_2,
        "value": val_value_2,
    }
    values.append(dict_value)

print(values)
