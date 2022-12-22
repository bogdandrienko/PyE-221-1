from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render

from django_api import models
from django_api import serializers as django_serializers


# Create your views here.

def index(request):
    # return HttpResponse("<h1>Hello world</h1>")
    return JsonResponse(data={
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }, safe=False)


def todos_native(request: HttpRequest, pk=-1) -> JsonResponse:
    if pk > 0:
        # match request.method:
        #     case "GET":
        #         def GET_one():
        #             # ONE
        #             # [1, +****)
        #             data = models.Todo.objects.get(id=pk)  # TODO QuerySet != JSON
        #             dict2 = {
        #                 "userId": data.user_id,
        #                 "id": data.id,
        #                 "title": data.title + str(" banana"),
        #                 "completed": data.completed,
        #                 # "created": data.completed,
        #             }
        #             # print(data, type(data))
        #             # dict1 = {
        #             #     "userId": 1,
        #             #     "id": 1,
        #             #     "title": "delectus aut autem",
        #             #     "completed": False
        #             # }
        #             return JsonResponse(data=dict2, safe=True)
        #         return GET_one()
        #     case "PUT" | "PATCH":
        #         pass
        #     case "DELETE":
        #         pass
        if request.method == "GET":
            # ONE
            # [1, +****)
            data = models.Todo.objects.get(id=pk)  # TODO QuerySet != JSON
            dict2 = {
                "userId": data.user_id,
                "id": data.id,
                "title": data.title + str(" banana"),
                "completed": data.completed,
                # "created": data.completed,
                # "updated": data.completed,
            }
            # print(data, type(data))
            # dict1 = {
            #     "userId": 1,
            #     "id": 1,
            #     "title": "delectus aut autem",
            #     "completed": False
            # }
            return JsonResponse(data=dict2, safe=True)
        elif request.method in ["PUT", "PATCH"]:
            #
            pass
        elif request.method == "DELETE":
            #
            return ""
    else:
        if request.method == "GET":
            # MANY
            data = models.Todo.objects.all()  # TODO QuerySet != JSON
            list_objects = []
            for d in data:
                dict2 = {
                    "userId": d.user_id,
                    "id": d.id,
                    "title": d.title + str(" banana"),
                    "completed": d.completed,
                    # "created": d.completed,
                }
                list_objects.append(dict2)
            return JsonResponse(data=list_objects, safe=False)
        if request.method == "POST":
            #
            return ""
    raise Exception("Method not allowed.")


# @permission_classes
@api_view(http_method_names=["GET", "POST", "PUT", "PATCH", "DELETE"])
def todos_drf(request: HttpRequest, pk="0") -> Response:
    pk = int(pk)
    if pk > 0:
        if request.method == "GET":
            # select title from todo where id = '2'
            data = models.Todo.objects.get(id=pk)  # TODO QuerySet != JSON
            # data.title
            data_json = django_serializers.TodoSerializer(instance=data, many=False).data
            return Response(data=data_json, status=status.HTTP_200_OK)
        elif request.method in ["PUT", "PATCH"]:
            #
            return ""
        elif request.method == "DELETE":
            models.Todo.objects.get(id=pk).delete()
            return Response(data={"detail": "Successfully deleted"}, status=status.HTTP_200_OK)
    else:
        if request.method == "GET":
            data = models.Todo.objects.all()  # TODO QuerySet != JSON
            data_json = django_serializers.TodoSerializer(instance=data, many=True).data
            return Response(data=data_json, status=status.HTTP_200_OK)
        if request.method == "POST":
            # { "user_id": 666, "title": "Emil", "completed": false }
            # request.GET
            # print(request.POST)
            # request.FILES
            print(request.data)
            # request.body

            # user_id = request.data["user_id"]
            user_id = request.data.get("user_id", 1)

            # title = request.data["title"]
            title = request.data.get("title", None)

            # completed = request.data["completed"]
            completed = request.data.get("completed", False)

            if title is None:
                return Response(data={"detail": "Not successfully created"}, status=status.HTTP_204_NO_CONTENT)
            models.Todo.objects.create(
                user_id=user_id,
                title=title,
                completed=completed
            )
            return Response(data={"detail": "Successfully created"}, status=status.HTTP_200_OK)
    raise Exception("Method not allowed.")
