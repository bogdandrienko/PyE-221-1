import requests
from bs4 import BeautifulSoup


value = 420000.6


url = 'https://finance.rambler.ru/calculators/converter/1-KZT-USD/'
# url = 'https://www.instagram.com/gazetakm/?hl=ru'
response = requests.get(url=url)
print(response)
print(response.status_code)
if response.status_code == 200:  # 200 - удачный ответ
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    print(type(soup))

    data = soup.find_all('div', class_='converter-display__cross-block')[0]
    new_data = str(data).split(sep='__value">')[1:]

    # [(1, 'KZT'), (0.0023, 'USD')]
    tenge = tuple(
        [
            new_data[0].split('</div>\n<div class="converter-display__currency">')[0],
            new_data[0].split('</div>\n<div class="converter-display__currency">')[1].split('</div>')[0]
        ]
    )
    print(tenge)
    print(type(tenge))

    dollar = tuple(
        [
            new_data[1].split('</div>')[0],
            new_data[1].split('</div>')[-3].split('>')[-1]
        ]
    )
    print(dollar)
    print(type(dollar))

    course = [tenge, dollar]
    print(course)
    print(type(course))

    # value
    index = 0
    for valute in course:
        index += 1
        print(f'Объект №{index}: {valute}')
        if valute[-1] == 'USD':
            result = round(value * float(valute[0]), 3)
            print(str(result) + " $")

    # print(new_data)
    # print(len(new_data))



    # content = response.content
    # with open(file='temp/new2.html', mode='wb') as file:
    #     file.write(content)

    # data = content.decode(encoding='ISO-8859-1')
    # print(type(data))
    # print(data)

    # new_data = data.split('value="')
    # print(len(new_data))
    # for i in new_data:
    #     print(i + '\n')
    # print(new_data)
else:
    print("ошибка получения данных!")
