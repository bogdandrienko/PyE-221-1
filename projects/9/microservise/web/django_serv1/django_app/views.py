import datetime
import json
import random
import threading
import time

import requests
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response


# Create your views here.

def index(request):
    context = {}
    return render(request, "index.html", context=context)


@api_view(http_method_names=["GET"])
@permission_classes([AllowAny])
def users(request: HttpRequest, pk="0") -> Response:
    pk = int(pk)
    if request.method == "GET":
        # users_objs = [
        #     {
        #         "id": x,
        #         "username": f"Python {x}",
        #         "date_joined": datetime.datetime.now(),
        #         "is_active": bool(random.randint(0, 1))
        #     } for x in range(1, 100 + 1)]
        # if pk > 0:
        #     users_objs = users_objs[pk - 1]
        # return Response(data=users_objs, status=status.HTTP_200_OK)
        if pk > 0:
            data = requests.get(f"http://127.0.0.1:8001/api/v2/users/{pk}")
        else:
            data = requests.get("http://127.0.0.1:8001/api/v2/users")

        # log(data.json())
        new_thread = threading.Thread(target=log, args=(data.json(),))
        new_thread.start()
        # new_thread.join()

        return Response(data=data.json(), status=status.HTTP_200_OK)
    return Response(data={}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


def log(data: dict):
    with open("log.json", mode="w") as file:
        json.dump(data, file)
        time.sleep(1.5)
