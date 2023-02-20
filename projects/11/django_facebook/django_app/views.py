from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
import asyncio

from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User, Group
from django_app import models
from django_app import forms

"""
Приложение для публикации постов (Post - сущность) - CRUD (CREATE - auth(login/logout), superuser/moder/user, , )




"""


def paginate(request, objects):
    paginator = Paginator(objects, 10)
    pages = request.GET.get('page')
    try:
        local_page = paginator.page(pages)
    except PageNotAnInteger:
        local_page = paginator.page(1)
    except EmptyPage:
        local_page = paginator.page(paginator.num_pages)
    return local_page


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Django app running...")


def json_index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"data": "anydata"}, safe=False, status=201)


def home(request: HttpRequest) -> HttpResponse:
    post1 = models.PostModel.objects.get(id=1)
    # form1 = forms.PostAdminForm()
    return render(request, 'django_app/home.html', {"post": post1})


def read(request: HttpRequest, post_id) -> HttpResponse:
    user = request.user
    author = models.PostModel.objects.get(id=post_id).author

    context = {"page": None, "is_my_post": user == author}
    return render(request, 'django_app/post_list.html', context=context)


class Product:
    def check_is_have(self):
        pass

    def add_if_unique(self):
        pass


def read_list(request: HttpRequest) -> HttpResponse:
    post_list = models.PostModel.objects.filter(is_moderate=True)
    page = paginate(request=request, objects=post_list)
    user = request.user
    list_owners = []
    for i in post_list:
        i.description = i.description[:10]
        list_owners.append({"post_id": i.id, "is_my_post": user.username == i.author.username})
    context = {"page": page, "list_owners": list_owners}

    return render(request, 'django_app/post_list.html', context=context)


def update(request: HttpRequest, post_id) -> HttpResponse:
    if request.method == 'POST':
        post = models.PostModel.objects.get(id=post_id)
        if post.is_moderate:
            post.is_moderate = False
        post.save()

    return redirect(reverse('app_name_django_app:read_list', args=()))


def delete(request: HttpRequest, post_id) -> HttpResponse:
    print("pass")
    return redirect(reverse('app_name_django_app:read_list', args=()))


class GetUsers(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        # await asyncio.sleep(1)
        print(User.objects.filter(is_active=True))
        return HttpResponse("Hello World!")
