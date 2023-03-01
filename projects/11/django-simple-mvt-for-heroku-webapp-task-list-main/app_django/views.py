from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.utils import timezone
from . import models


# Create your views here.
def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect(reverse('app_name_task_list:home', args=()))
    return render(request, 'pages/register.html', context={})


def sing_in(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)  # Сохраняет текушую сессию в cookies browser
            return redirect(reverse('app_name_task_list:home', args=()))
        else:
            raise Exception("Логин или пароль не верны!")
    return render(request, 'pages/login.html')


def logout_(request):
    logout(request)
    return redirect(reverse('app_name_task_list:home', args=()))


def index(request):
    return HttpResponse("<h1>This is a Index Page</h1>")


def home(request):
    context = {
    }
    return render(request, 'pages/home.html', context)


def post(request):
    posts = models.Post.objects.all()
    post_comment = models.PostComment.objects.filter(article=posts[0])
    print(post_comment)
    # post = models.Post.objects.get(id=post_id)
    context = {
        'names':
            posts
    }
    return render(request, 'pages/Post_detail.html', context)


def post_detail(request: HttpRequest, pk: int):
    post_ = models.Post.objects.get(id=pk)
    context = {
        "posts": post_
    }
    return render(request, 'app_task_list/pages/post_detail.html', context=context)


def create(request):
    if request.method == 'POST':
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        models.Task.objects.create(
            author=request.user,
            title=title,
            description=description,
            is_completed=False,
        )
        return redirect(reverse('app_name_task_list:read_list', args=()))
    context = {
    }
    return render(request, 'app_task_list/pages/task_create.html', context)


def read(request, task_id=None):
    task = models.Task.objects.get(id=task_id)
    context = {
        "task": task
    }
    return render(request, 'app_task_list/pages/task_detail.html', context)


def read_list(request):
    is_detail_view = request.GET.get("is_detail_view", True)
    if is_detail_view == "False":
        is_detail_view = False
    elif is_detail_view == "True":
        is_detail_view = True
    task_list = models.Task.objects.all()

    def paginate(objects, num_page):
        paginator = Paginator(objects, num_page)
        pages = request.GET.get('page')
        try:
            local_page = paginator.page(pages)
        except PageNotAnInteger:
            local_page = paginator.page(1)
        except EmptyPage:
            local_page = paginator.page(paginator.num_pages)
        return local_page

    page = paginate(objects=task_list, num_page=4)
    context = {
        "page": page,
        "is_detail_view": is_detail_view
    }
    return render(request, 'app_task_list/pages/task_list.html', context)


def update(request, task_id=None):
    if request.method == 'POST':
        task = models.Task.objects.get(id=task_id)
        is_completed = request.POST.get("is_completed", "")
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        if is_completed:
            if is_completed == "False":
                task.is_completed = False
            elif is_completed == "True":
                task.is_completed = True
        if title and title != task.title:
            task.title = title
        if description and description != task.description:
            task.description = description
        task.updated = timezone.now()
        task.save()
        return redirect(reverse('app_name_task_list:read_list', args=()))
    task = models.Task.objects.get(id=task_id)
    context = {
        "task": task
    }
    return render(request, 'app_task_list/pages/task_change.html', context)


def delete(request, task_id=None):
    # models.Task.objects.get(id=task_id).delete()
    task = models.Task.objects.get(id=task_id)
    if task.author == request.user:
        task.delete()
    else:
        pass  # TODO Logging invalid action

    return redirect(reverse('app_name_task_list:read_list', args=()))


def post_ph(request, post_id=None):
    print(post_id)
    post_new = models.Post.objects.get(id=post_id)
    comment_new = models.PostComment.objects.filter(article=post_new)
    print(comment_new)
    context = {
        "post": post_new,
        'comments': comment_new
    }
    return render(request, 'app_task_list/pages/post_detail.html', context)


def post_comment_create(request):
    pass
