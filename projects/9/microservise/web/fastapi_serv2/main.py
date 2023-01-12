import datetime
import random
from typing import Union
from fastapi import FastAPI
import psycopg2

app = FastAPI()


class User:
    def __init__(self, _id: int, username: str, date_joined: datetime.datetime, active: bool):
        self._id = _id
        self._username = username
        self._date_joined = date_joined
        self._active = active

    @staticmethod
    def serialize(row_from_database: tuple):
        _id = row_from_database[0]
        _username = row_from_database[1]
        _date_joined = row_from_database[2]
        _active = row_from_database[3]
        return User(_id=_id, username=_username, date_joined=_date_joined, active=_active)

    @staticmethod
    def get_all_users():
        connection = None
        cursor = None

        try:
            connection = psycopg2.connect(
                user="example_micro_usr",
                password="12345Qwerty!",
                host="127.0.0.1",
                port="5432",
                dbname="example_micro_db",
            )
            cursor = connection.cursor()
            query_string1 = "select * from users order by id asc"
            cursor.execute(query_string1)
            records = cursor.fetchall()
            users = [User.serialize(record) for record in records]
        except Exception as err:
            print(err)
            return None
        else:
            return users
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def get_one_user(pk: int):
        connection = None
        cursor = None

        try:
            connection = psycopg2.connect(
                user="example_micro_usr",
                password="12345Qwerty!",
                host="127.0.0.1",
                port="5432",
                dbname="example_micro_db",
            )
            cursor = connection.cursor()
            query_string1 = f"select * from users where id = {pk}"
            cursor.execute(query_string1)
            record = cursor.fetchone()
            users = User.serialize(record)
        except Exception as err:
            print(err)
            return None
        else:
            return users
        finally:
            cursor.close()
            connection.close()


@app.get("/api/v2/users")
async def read_root_1():
    return User.get_all_users()


@app.get("/api/v2/users/{pk}")
async def read_root(pk: str):
    return User.get_one_user(int(pk))
