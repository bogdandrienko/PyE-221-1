from flask import Flask, render_template, request, redirect, url_for
import requests
from bs4 import BeautifulSoup
import psycopg2

app = Flask(__name__, template_folder='../template', static_url_path='/static', static_folder='../static')
url = 'https://kolesa.kz/mototehnika/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/77.0.3865.90 Safari/537.36"}


@app.route("/temp/")
def temp():
    return render_template('temporary.html')


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

        return render_template('login.html', status=200)
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


@app.route("/todo_create/", methods=['POST'])
def todo_create():
    username = request.form.get('username')
    salary = request.form.get('salary')

    connection_string = "dbname='flask_database' user='flask_user' host='localhost' password='12345qwertY!'"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    connection.autocommit = False
    try:
        cursor.execute(f"""INSERT INTO zarplata (username, salary) VALUES ('{str(username)}', '{int(salary)}');""")
    except Exception as error:
        connection.rollback()
        print(error)
    else:
        connection.commit()
    finally:
        cursor.close()
        connection.close()
    return redirect(url_for('todo_list'))


@app.route("/todo_list/", methods=['GET'])
def todo_list():
    todos = []
    connection_string = "dbname='flask_database' user='flask_user' host='localhost' password='12345qwertY!'"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    connection.autocommit = False
    try:
        cursor.execute("""select * from zarplata;""")
        # print(10 - "")  #
        # print({"name": "Bogdan"}["username"])  #
        data = cursor.fetchall()
        print(data)
        todos = data
    except Exception as error:
        connection.rollback()
        print(error)
    else:
        connection.commit()
    finally:
        cursor.close()
        connection.close()

    todos_temp = []
    if len(todos) > 0:
        for i in todos:
            todos_temp.append({"id": i[0], "name": i[1], "salary": i[2]})
    todos = todos_temp

    # todos = [{"id": x, "name": f"Clear cat #{x}", "salary": 60000 + x * 100} for x in range(1, 30+1)]
    return render_template('Todo_list.html', todos=todos)  # **kwargs


@app.route("/todo_detail/<todo_id>/", methods=['GET'])
def todo_detail(todo_id):
    todo = {}
    connection_string = "dbname='flask_database' user='flask_user' host='localhost' password='12345qwertY!'"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    connection.autocommit = False
    try:
        cursor.execute(f"""select * from zarplata where id = '{todo_id}';""")
        # print(10 - "")  #
        # print({"name": "Bogdan"}["username"])  #
        data = cursor.fetchone()
        print(data)
        todo = data
    except Exception as error:
        connection.rollback()
        print(error)
    else:
        connection.commit()
    finally:
        cursor.close()
        connection.close()

    if todo is not None:
        todo = {"id": todo[0], "name": todo[1], "salary": todo[2]}
    else:
        todo = {}

    return render_template('Todo_detail.html', todo=todo)  # **kwargs


def db():
    # connection_string = "dbname='flask_database' user='postgres' host='localhost' password='31284bogdan'"
    connection_string = "dbname='flask_database' user='flask_user' host='localhost' password='12345qwertY!'"
    connection = psycopg2.connect(connection_string)
    cursor = connection.cursor()
    connection.autocommit = False
    try:
        cursor.execute("""INSERT INTO zarplata (username, salary) VALUES ('Bogdan', '60000'), ('Alice', '80000');""")
        cursor.execute("""select * from zarplata;""")
        # print(10 - "")  #
        # print({"name": "Bogdan"}["username"])  #
        data = cursor.fetchall()
        print(data)
        print(len(data))
        print(10 / 0)  # ZEROdivision
    except Exception as error:
        connection.rollback()
        print(error)
    else:
        connection.commit()
    finally:
        cursor.close()
        connection.close()
