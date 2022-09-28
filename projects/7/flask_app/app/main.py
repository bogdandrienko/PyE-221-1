from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__, template_folder='../template')
url = 'https://kolesa.kz/mototehnika/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/77.0.3865.90 Safari/537.36"}


@app.route("/")
def home():
    users = [{"name": f"Alice ({x + 18})", "age": x + 18} for x in range(1, 100 + 1)]
    print(users)

    user = {"name": f"Alice (18)", "age": 18}

    return render_template('home.html', price=666, user=user, users=users)


@app.route("/login/", methods=['GET', 'POST'])
def login():

    if request.method == "GET":
        import json
        with open('temp/db.json', 'r') as file:
            # print('\n\n\n\n\n!!!!!!!!!!\n\n\n\n')
            json_obj = json.load(file)
            # print(f"json_obj: {json_obj}")
            return render_template(
                'login.html',
                username=json_obj["username"],
                password=json_obj["password"]
            )
    elif request.method == "POST":
        # послать с фронтенда данные (заполненную форму для регистрации пользователя)

        print(request.args)

        email = request.form.get('email')
        password = request.form.get('password')

        # email = request.args.get('email')
        # password = request.args.get('password')

        print(f"email: {email}")
        print(f"email: {password}")

        # email = "Alice"
        # password = "qwerty12345"

        import json
        with open('temp/db.json', 'w') as file:
            print('\n\n\n\n\n!!!!!!!!!!\n\n\n\n')
            json.dump({"username": email, "password": password}, file)

        with open('temp/data.txt', 'w') as file:
            file.write(f"{email}\n")
            file.write(f"{password}\n")

        return render_template('login.html')
    else:
        return "<h1>METHOD NOT ALLOWED</h1>"


@app.route("/parse/")
def parse():
    response = requests.get(url=url, headers=headers)
    data1 = response.text
    bs4Obj = BeautifulSoup(data1, 'html.parser')

    class Vehicle:
        def __init__(self, price, city, model, description, url, name, phone):
            self.phone = phone
            self.name = name
            self.url = url
            self.model = model
            self.description = description
            self.city = city
            self.price = price

    objects = bs4Obj.find_all('div', class_="a-list__item")  # вся техника!
    print(len(objects))

    lists = ""
    for obj in objects:
        try:
            # вытаскиваем цену одного транспорта
            price = int(
                ''.join(str(obj.find('span', class_="a-card__price")).split('>')[1].split('<')[0].strip().split()))

            # вытаскиваем модель одного транспорта
            # model = str(''.join(str(obj.find('a', class_="a-card__link")).split('>')[1].split('<')[0].strip().split()))
            model = str(obj.find('h5', class_="a-card__title")).split('</a>')[0].split('target="_blank">')[1].strip()
            print(f"{model}: {price}")
            print('\n\n\n*********************************************************\n\n\n')
            lists += f"<li><strong>{model}</strong>: {price}</li>"
        except Exception as error:
            pass
    # sep1 = 'class="a-list"'
    # data2 = data1.split(sep=sep1)[1]
    # print(data2)

    return f"<ul>{lists}</ul>"
