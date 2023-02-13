import random

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests
import threading
from django_app import tasks as django_app_celery
from django_settings.celery import app as current_celery_app
from celery.result import AsyncResult


# Create your views here.

def home(request):
    if request.method == "POST":
        def log():
            requests.post(
                "http://127.0.0.1:8000/api/logger",
                json={"text": request.POST["text"], "count": 666, "is_hide": False}
            )

        threading.Thread(target=log).start()
    return render(request, "Home.html")


def books(request):
    data = requests.get("http://127.0.0.1:8000/home").json()
    return JsonResponse(data)


def celer(request):
    # bulk_mail
    # for i in messages
    """
    Для улучшения пользовательского опыта, продолжительные процессы должны
    выполняться в фоновом режиме вне обычного потока HTTP-запросов/ответов.
    Например:

    Отправка писем для подтверждения;
    Парсинг;
    Анализ данных;
    Обработка изображений;
    Генерация отчетов.


    При создании приложения, старайтесь отделять задачи, которые должны выполняться в
    течение жизненного цикла запроса/ответа, например CRUD-операции, от задач, которые
    должны выполняться в фоновом режиме.
    """

    """
    # shell
    sudo apt update -y
    sudo apt install -y redis
    redis-server
    redis-cli
    ping # PONG
    exit
    # shell
    """

    # pip install celery
    # pip install django-redis
    # python -m celery -A django_settings worker -l info

    # task_id = django_app_celery.add(random.randint(1, 10), random.randint(1, 10))  # прямой вызов
    # task_id = django_app_celery.add.apply_async((random.randint(1, 10), random.randint(1, 10)))  # *ARGS
    # print(task_id)
    #
    # # c6f55087-2769-4df4-8945-244693faa416

    # TODO GET RESULT FROM CELERY
    task_id = "e72e0e48-6b0e-4251-9987-0af833f6c592"
    result = AsyncResult(task_id, app=current_celery_app)
    if result.state == "SUCCESS":
        res = f"{result.state} {result.get()}"
    else:
        res = f"{result.state} {None}"

    # 1 init
    # 2 send
    # 3 in progress
    # 4 completed
    # 5 failed

    # task_id = django_app_celery.send_mass_mail.apply_async()  # **KWARGS
    # print(task_id)
    # # # первый запрос - начинаем рассылку сотни писем
    # res = ""

    # task_id = ""
    # res = django_app_celery.send_mass_mail()

    return HttpResponse(f"<h1>Task_id: {task_id} [{res}]</h1>")


def start(request):
    # TODO START CELERY TASK
    task_id = django_app_celery.send_mass_mail.apply_async()
    return HttpResponse(f"<h1>Task_id: {task_id}</h1>")
