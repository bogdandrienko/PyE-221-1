import flask
from flask import Flask
import psycopg2
from flask import jsonify
from flask import request

# Model View Controller

# 127.0.0.1:5432 (localhost:5432) - текущая машина, откуда идёт запрос
# 192.168.1.121:5432 - локальный адрес текущей машины в этой подсети
# 89.218.132.130:80 - внешний "белый" ip-адрес от Казактелекома
# km.kz - домен первого уровня
# web.km.kz (89.218.132.130) - домен второго уровня

app = Flask(__name__)


@app.route("/index")  # 'http://192.168.1.121:5000' + '/' - маршрут в браузерной строке
def index():
    return "<h1>Index</h1>"


@app.route("/about")
def about():
    return flask.render_template('about.html')


@app.route("/")
def home():
    return flask.render_template('home.html')


@app.route("/todo_create", methods=['GET', 'POST'])
def todo_create():
    if request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')
        status = request.form.get('status', False)

        print(f"title: {title}")
        print(f"description: {description}")
        print(f"status: {status}")

        conn = psycopg2.connect("dbname=flask_db user=postgres password=31284bogdan")
        cur = conn.cursor()

        query_string = f"""
        INSERT INTO public.flask_table (title, description, status) 
        VALUES ('{title}', '{description}', '{status}')
        """
        cur.execute(query_string)
        conn.commit()
        cur.close()
        conn.close()

    return flask.render_template('todo_create.html')


@app.route("/todo_list")  # 'http://192.168.1.121:5000' + '/' - маршрут в браузерной строке
def todo_list():
    conn = psycopg2.connect("dbname=flask_db user=postgres password=31284bogdan")
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM public.flask_table
    ORDER BY id ASC
    """)
    records = cur.fetchall()
    cur.close()
    conn.close()
    task_list = [{"title": x[0], "description": x[1][:5], "status": x[2], "id": x[3]} for x in records]

    print(task_list)
    print(type(task_list))

    context = {
        "task_list": task_list,
        "username": "Роман"
    }
    return flask.render_template('todo_list.html', **context)


@app.route("/todo/<todo_id>")  # 'http://192.168.1.121:5000' + '/' - маршрут в браузерной строке
def todo_by_id(todo_id):
    conn = psycopg2.connect("dbname=flask_db user=postgres password=31284bogdan")
    cur = conn.cursor()

    cur.execute(f"""
        SELECT * FROM public.flask_table
        WHERE id = '{todo_id}'
        """)
    record = cur.fetchall()[0]
    cur.close()
    conn.close()
    print(record)
    record = {
        "title": record[0], "description": record[1],
        "status": record[2], "id": record[3]
    }
    return flask.render_template('todo_detail.html', task=record)


@app.route("/get_all_rows/")
def get_all_rows():
    conn = psycopg2.connect("dbname=example user=postgres password=31284bogdan")
    cur = conn.cursor()
    query_string = """
    SELECT * FROM public.example_table
    ORDER BY id ASC
    """
    cur.execute(query_string)
    records = cur.fetchall()
    cur.close()
    conn.close()
    data = jsonify(records)
    return data

# Страница с добавлением задачи                (POST) Create / Insert
# Страница с просмотром всех задач             (GET) Get all / Select
# Страница с просмотром детально одной задачи  (GET) Get one / Select
# Функция для удаления задачи                  (DELETE) DELETE one / DELETE
# Страничка с обновлением уже существующей     (PUT) UPDATE / UPDATE
