import datetime
import time
from collections import OrderedDict

from _decimal import Decimal
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import render
import psycopg2
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from django_app import serializers, models


# python manage.py runserver 0.0.0.0:8000

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        pass
    else:
        pass

    return render(request, "build/index.html")  # public/index.html


from abc import ABC, abstractmethod


class Figure(ABC):
    p = 3.14

    def __new__(cls, *args, **kwargs):
        pass

    @classmethod
    def perimeter1(cls):
        # new = cls()
        return 0

    @staticmethod
    def perimeter():
        return 0

    @abstractmethod
    def square(self):
        return 0


fg = Figure()


class Triangle(Figure):
    def square(self):
        return 0


class Mother:
    eyes = "brown"
    pass


class Father:
    eyes: str = "blue"
    height: float = 1.9
    pass


father1 = Father()
print(father1.eyes)


class Grand:
    math: Decimal = 5.0
    math1: OrderedDict = {"name": "Alysa"}

    def __init__(self, surname: str):
        self.surname = surname


class Child(Mother, Father, Grand):
    age: int = 18  # class attribute

    # хранение данных, принадлежащих к классу в целом и редко изменяющихся

    def __init__(self, name: str):
        super().__init__("_" + name)
        self.name = name  # instance attribute
        # хранение данных, принадлежащих преимущественно к этому объекту


Child.age = "66"  # dynamic
# print(Child.age / 10)
# print(Child.name)

child = Child("Alice")
print(child.name)


class GetAllTodos(LoginRequiredMixin, View):
    login_url = '/login/'  # /accounts/login/?next=/class/

    # redirect_field_name = 'redirect_to'

    def get(self, request):
        # Perform io-blocking view logic using await, sleep for example.
        return HttpResponse(f"Hello async world! ({datetime.datetime.now()})")

    def post(self, request):
        # Perform io-blocking view logic using await, sleep for example.
        return HttpResponse(f"Hello async world! ({datetime.datetime.now()})")

    def put(self, request):
        # Perform io-blocking view logic using await, sleep for example.
        return HttpResponse(f"Hello async world! ({datetime.datetime.now()})")

    def delete(self, request):
        # self.serialize()
        # Perform io-blocking view logic using await, sleep for example.
        return HttpResponse(f"Hello async world! ({datetime.datetime.now()})")

    def serialize(self):
        pass


class Todo:
    def __init__(self, id_: int, title: str, description: str, status: bool, datetime_: datetime.datetime):
        self.id_ = id_
        self.title = title
        self.description = description
        self.status = status
        self.datetime_ = datetime_

    @staticmethod
    def get_all_todos(query: str) -> list[tuple]:
        with psycopg2.connect(
                user="django_pgs_usr",
                password="12345Qwerty!",
                host="127.0.0.1",
                port="5432",
                dbname="django_pgs_db"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                rows = cursor.fetchall()
                if rows is None:
                    raise Exception("No have data!")
        return rows


def todos(request):
    rows = Todo.get_all_todos("select * from todos order by id desc;")
    # rows = models.Todo.objects.all().order_by("-id")
    objs = [
        {"id": row[0], "title": row[1], "description": row[2], "status": row[3], "datetime": row[4]}
        for row in rows
    ]
    return JsonResponse(data=objs, safe=False)


def todos_id(request, todo_id):
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
    return JsonResponse(data=obj, safe=False)


@api_view(['GET'])
def routes(request):
    return Response(data={"Все маршруты начинаются с :": {"/todos": "тудушки", "/users": "пользователи"}})


def get_all_users1(request: HttpResponse) -> JsonResponse:
    users_python_like = User.objects.all()
    users_json_like = [{"username": usr.username, "password": usr.password} for usr in users_python_like]
    return JsonResponse(data=users_json_like, safe=False)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def get_all_users(request: Request) -> Response:
    users_python_like = User.objects.all()  # DataBase ORM
    users_json_like = serializers.UserSerializer(instance=users_python_like, many=True).data
    return Response(data=users_json_like, status=status.HTTP_200_OK)


def database():
    # C:\Program Files\PostgreSQL\15\bin
    # cmd
    # \l
    # \d
    # CREATE USER django_pgs_usr WITH PASSWORD '12345Qwerty!';
    # CREATE DATABASE django_pgs_db OWNER django_pgs_usr;
    # \connect django_pgs_db;
    """

CREATE TABLE PUBLIC.TODOS
  (
     ID          SERIAL PRIMARY KEY,
     TITLE       VARCHAR(255) UNIQUE NOT NULL,
     DESCRIPTION VARCHAR(1024) DEFAULT '',
     STATUS      BOOL DEFAULT 'false',
     DATETIME    TIMESTAMP DEFAULT NOW()
  );

    """
    # \d
    # GRANT ALL PRIVILEGES ON DATABASE django_pgs_db TO django_pgs_usr;
    # GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to django_pgs_usr;
    # GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to django_pgs_usr;
    # GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to django_pgs_usr;

    # select * from todos;
    # insert into todos (title, description, status) VALUES ('Buy a cat', 'Buy a cat Buy a cat', 'true');
    # insert into todos (title, description, status) VALUES ('Buy a cat 2', 'Buy a cat 2 Buy a cat 2', 'true');
    # insert into todos (title, description, status) VALUES ('Buy a cat 3', 'Buy a cat 3 Buy a cat 3', 'false');
    # insert into todos (title, description, status) VALUES ('Buy a cat 4', 'Buy a cat 4 Buy a cat 4', 'true');

    # delete from todos where id=1;

    # \q
    pass


@api_view(['GET', 'POST'])
def todos_new(request: Request) -> Response:
    try:
        if request.method == "GET":
            _todos_obj = models.Todo.objects.all()
            _todos_json = serializers.TodoSerializer(instance=_todos_obj, many=True).data
            return Response(data={"response": _todos_json}, status=status.HTTP_200_OK)
        if request.method == "POST":
            # {"title": "Купить кота"}
            title = request.data.get("title", None)
            if title is None:
                raise Exception("Title not have!")
            models.Todo.objects.create(
                title=title
            )
            return Response(data={"response": "Успешно создано!"}, status=status.HTTP_201_CREATED)
    except Exception as error:
        print("error", error)
        return Response(data={"error": str(error)}, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def todos_new_id(request: Request, pk: int) -> Response:
    try:
        if request.method == "GET":
            _todos_obj = models.Todo.objects.get(id=pk)
            _todos_json = serializers.TodoSerializer(instance=_todos_obj, many=False).data
            return Response(data={"response": _todos_json}, status=status.HTTP_200_OK)
        if request.method == "PUT":
            # {"title": "Купить кота"}
            title = request.data.get("title", None)
            if title is None:
                raise Exception("Title not have!")
            obj = models.Todo.objects.get(id=pk)
            if obj.title != title:
                obj.title = title
                obj.save()
            return Response(data={"response": "Успешно обновлено!"}, status=status.HTTP_200_OK)
        if request.method == "DELETE":
            models.Todo.objects.get(id=pk).delete()
            return Response(data={"response": "Успешно удалено!"}, status=status.HTTP_200_OK)
    except Exception as error:
        print("error", error)
        return Response(data={"error": str(error)}, status=status.HTTP_200_OK)
