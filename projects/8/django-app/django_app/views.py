import random

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render

from django_app import models as django_models


# Create your views here.
# TODO контроллер-класс
#


# TODO контроллер-функция
def index(request):
    # generator1 = ({"id": random.randint(0, x), "name": f"Bogdan {x}", "age": x + 20} for x in range(1, 100))

    context = {
        'Name': "Bogdan",
        'list1': [{"id": random.randint(0, x), "name": f"Bogdan {x}", "age": x + 20} for x in range(1, 100)]
        # 'this_user_has_access_to_navbar': groups = Group.objects.all()
        # 'this_user_has_access_to_navbar': groups = Group.objects.all()
        # 'this_user_has_access_to_navbar': groups = Group.objects.all()
    }
    # return HttpResponse(content=b"<h1>Hello World</h1>")
    # return JsonResponse(data={"response": 'res'}, safe=True)
    return render(request, 'django_app/home.html', context=context)


def get_words(count: int) -> str:
    result = ""
    idx = 1
    while True:
        result += random.choice(["Alfa ", "Betta ", "Gamma ", "Omega "])
        if idx == count:
            break
        idx += 1
    return result.strip()


def get_password(length: int, chars="1234567890!@#$%ABCDEFGabcdef", append_chars="") -> str:
    result = ""
    idx = 1
    while True:
        result += random.choice(chars + append_chars)
        if idx == length:
            break
        idx += 1
    return result.strip()


def post(request: HttpRequest, post_id: int) -> JsonResponse:
    x = post_id - 1
    list_comprehension1 = {
        "userId": round(x / 10, 0),
        "id": x,
        "title": get_words(count=1),
        "body": get_words(count=random.randint(3, 7))
    }

    return JsonResponse(data=list_comprehension1, safe=False)


def posts(request: HttpRequest) -> JsonResponse:
    print("password: ", get_password(length=8, append_chars="_-="))
    # generator1 = (
    #     {
    #         "userId": round(x / 10, 0),
    #         "id": x,
    #         "title": get_words(count=1),
    #         "body": get_words(count=random.randint(3, 7))
    #     }
    #     for x in range(1, 10)
    # )
    # print("generator1: ", generator1, type(generator1))

    list_comprehension1 = [
        {
            "userId": round(x / 10, 0),
            "id": x,
            "title": get_words(count=1),
            "body": get_words(count=random.randint(3, 7))
        }
        for x in range(1, 100 + 1)
    ]

    return JsonResponse(data=list_comprehension1, safe=False)


def todo(request: HttpRequest, todo_id=0) -> JsonResponse:
    # TODO Create (POST)
    # TODO insert into Todo (user, title) VALUES ('123', "321")
    # todo_obj = django_models.Todo.objects.create(
    #     user=1234,
    #     title="4321",
    # )
    # TODO Create (POST)

    # TODO Read (GET = one | array)
    # TODO select * from Todo where id = 1
    # todo_obj = django_models.Todo.objects.get(id=1)
    # print("todo_obj: ", todo_obj, type(todo_obj))
    # TODO select * from Todo
    # todo_objs = django_models.Todo.objects.all()
    # print("todo_objs: ", todo_objs, type(todo_objs))
    # TODO select * from Todo where title = "321"
    # todo_objs = django_models.Todo.objects.filter(title="321")
    # TODO select * from Todo order by user, title
    # todo_objs = django_models.Todo.objects.order_by("user", "title")
    # TODO select count(*) from Todo
    # todos_count = django_models.Todo.objects.all().count()
    # TODO Read (GET = one | array)

    # Update (PUT)
    # TODO update Todo set user = '111', title = "3333333" where id = 3;
    # todo_obj = django_models.Todo.objects.get(id=3)
    # print("todo_obj: ", todo_obj, type(todo_obj))
    # todo_obj.user = 111
    # todo_obj.title = "3333333"
    # todo_obj.save()
    # Update (PUT)

    # Delete (DELETE)
    # TODO delete from Todo where id = 1
    # todo_obj = django_models.Todo.objects.get(id=1).delete()
    # Delete (DELETE)

    result = None
    if todo_id > 0:
        if request.method == "GET":
            # TODO select * from Todo where id = todo_id
            todo_obj = django_models.Todo.objects.get(id=todo_id)  # Todo1
            result = {"id": todo_obj.id, "user": todo_obj.user, "title": todo_obj.title}  # ручная сериализация
        elif request.method == "PUT":
            user = 111
            title = "3333333"

            # TODO update Todo set user = '111', title = "3333333" where id = 3;
            todo_obj = django_models.Todo.objects.get(id=todo_id)
            todo_obj.user = user
            todo_obj.title = title
            todo_obj.save()

            result = "Успешно обновлено"
        elif request.method == "DELETE":
            # TODO delete from Todo where id = 1
            django_models.Todo.objects.get(id=todo_id).delete()

            result = "Успешно удалено"
        else:
            pass
    else:
        match request.method:
            case "GET":
                # TODO select * from Todo
                todo_objs = django_models.Todo.objects.all()  # [Todo1, Todo2...]
                result = []
                for i in todo_objs:
                    result.append(
                        {"id": i.id, "user": i.user, "title": i.title}  # ручная сериализация
                    )
            case "POST":
                user = 1234
                title = "4321"

                # TODO insert into Todo (user, title) VALUES ('123', "321")
                django_models.Todo.objects.create(
                    user=user,
                    title=title,
                )

                result = "Успешно создано"
            case _:
                pass
    return JsonResponse(data=result, safe=False)
