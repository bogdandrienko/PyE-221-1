from typing import Union

import psycopg2
from fastapi import FastAPI

app = FastAPI()


# uvicorn main:app --reload --host=0.0.0.0

@app.get("/todos")
async def todos():
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


@app.get("/todos/{todo_id}")
async def todos_id(todo_id):
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
