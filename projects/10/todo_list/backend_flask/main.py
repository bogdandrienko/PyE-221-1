from flask import Flask, request
import psycopg2

app = Flask(__name__)


# flask --app main --debug run --host=0.0.0.0 --port=8000
# curl -v -X GET 127.0.0.1:8000/todos
# curl -v -X GET 127.0.0.1:8000/todos/1
# curl -v -X POST -H 'username:Python' 127.0.0.1:8000/todos/create -d '{"title":"Python is awesome!"}'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/todos", methods=['GET'])
def todos():
    connection = psycopg2.connect(
        user="todolist_usr",
        password="12345Qwerty!",
        host="127.0.0.1",
        port="5432",
        dbname="todolist_db",
    )
    cursor = connection.cursor()
    cursor.execute("select * from todos;")
    rows = cursor.fetchall()
    if rows is None:
        raise Exception("No data!")
    objs = [
        {"id": row[0], "title": row[1], "description": row[2], "date_create": row[3], "status": row[4]}
        for row in rows
    ]
    return objs


@app.route("/todos/<todo_id>", methods=['GET'])
def todos_id(todo_id):
    connection = psycopg2.connect(
        user="todolist_usr",
        password="12345Qwerty!",
        host="127.0.0.1",
        port="5432",
        dbname="todolist_db",
    )
    cursor = connection.cursor()
    cursor.execute(f"select id, title, description, date_create, status from todos where id='{todo_id}';")
    row = cursor.fetchone()
    if row is None:
        raise Exception("No data!")
    obj = {"id": row[0], "title": row[1], "description": row[2], "date_create": row[3], "status": row[4]}
    return obj


@app.route("/todos/create", methods=['GET', 'POST'])
def todos_create():
    # title = request.form.get("title")  # form multipart/form-data
    # print(title, type(title))

    # print("1 ", request.form.to_dict())
    # print("2 ", request.values)
    # print("3 ", request.json)
    # print("4 ", request.data)

    # connection = psycopg2.connect(
    #     user="todolist_usr",
    #     password="12345Qwerty!",
    #     host="127.0.0.1",
    #     port="5432",
    #     dbname="todolist_db",
    # )
    # cursor = connection.cursor()
    # cursor.execute(f"select id, title, description, date_create, status from todos where id='{todo_id}';")
    # row = cursor.fetchone()
    # if row is None:
    #     raise Exception("No data!")
    # obj = {"id": row[0], "title": row[1], "description": row[2], "date_create": row[3], "status": row[4]}
    return {}
