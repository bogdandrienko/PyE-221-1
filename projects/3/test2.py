import requests
from bs4 import BeautifulSoup

url = "https://myfin.by/converter.html"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}
response = requests.get(url=url, headers=headers)
status = response.status_code
if status == 200:
    content = response.content  # позволяет прочитать html фаил
    with open("temp/hw.html", "wb") as file:  # создаем фаил куда запишем html код
        file.write(content)  # записывае фаил
    soup = BeautifulSoup(response.text, "lxml")  # парсим саит через BeautifulSoup
    # print(type(soup))
    data = soup.findAll("input", class_="input_calc form-control form-input-sum bestmb") # Ищем по html
    new_data = str(data).split(sep='inputmode="decimal" type="tel" value="')
    new_data = str(new_data).split(sep='<input class="input_calc form-control form-input-sum bestmb" id="bestmb_')
    # print(new_data[6])
    dollar1 = new_data[1].split("""', '""")[0].split('"')[0]
    dollar2 = new_data[1].split("""usd" ', '""")[1].split('"/>')[0]
    dollar = tuple([dollar2, dollar1])
    # print(type(dollar))
    euro1 = new_data[2].split("""', '""")[0].split('"')[0]
    euro2 = new_data[2].split("""eur" ', '""")[1].split('"/>')[0]
    euro = tuple([euro2, euro1])
    # print(euro)
    sterling1 = new_data[3].split("""', '""")[0].split('"')[0]
    sterling2 = new_data[3].split("""gbp" ', '""")[1].split("/>,")[0].split('"')[0]
    sterling = tuple([sterling2, sterling1])
    # print(sterling2)
    uany1 = new_data[4].split("""', '""")[0].split('"')[0]
    uany2 = new_data[4].split("""cny" ', '""")[1].split('"/>')[0]
    uany = tuple([uany2, uany1])
    # print(uany)
    zloty1 = new_data[5].split("""', '""")[0].split('"')[0]
    zloty2 = new_data[5].split("""pln" ', '""")[1].split('"/>')[0]
    zloty = tuple([zloty2, zloty1])
    # print(zloty)
    rub1 = new_data[6].split("""', '""")[0].split('"')[0]
    rub2 = new_data[6].split("""rub" ', '""")[1].split('"/>')[0]
    rub = tuple([rub2, rub1])
    # print(rub)
    cours = [dollar, euro, sterling, uany, zloty, rub]
    # print(cours)
    value = 450000

    for valute in cours:
        # print(valute)
        if valute[-1] == "eur":
            result = value * float(valute[0])
            print(valute[0])
            print(result)





        # for i in new_data:
        #     print(i)
        #     print(len(i))
        #     # print('\n')
        # print('\n')
else:
    print("Oshibka dannyh")