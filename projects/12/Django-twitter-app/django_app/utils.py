import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse


def paginate(request, objects, num_page):
    paginator = Paginator(objects, num_page)
    pages = request.GET.get("page")
    try:
        local_page = paginator.page(pages)
    except PageNotAnInteger:
        local_page = paginator.page(1)
    except EmptyPage:
        local_page = paginator.page(paginator.num_pages)

    return local_page


def login_required_decorator(func):
    def wrapper(*args, **kwargs):
        request = args[0]
        if not request.user.is_authenticated:
            return redirect(reverse("django_app:login", args=()))

        response = func(*args, **kwargs)
        return response

    return wrapper


def logging_txt_decorator(func):
    def wrapper(*args, **kwargs):
        request: HttpRequest = args[-1]
        print(request.user)

        if request.user.is_anonymous:
            username = "Аноним"
        else:
            username = request.user.username
        with open("static/log.txt", 'a', encoding="utf-8") as file:
            file.write(f"{username} | {request.path} | {request.method} | {datetime.datetime.now()}\n")

        response = func(*args, **kwargs)
        return response

    return wrapper


def caching(cache, name, timeout=10, query=lambda: None):
    data = cache.get(name)
    if not data:
        data = query()
        cache.set(name, data, timeout=timeout)
    return data
