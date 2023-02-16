from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
import asyncio
from django.views import View
from django.contrib.auth.models import User, Group


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Django app running...")


def json_index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"data": "anydata"}, safe=False, status=201)


def homepage(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


class GetUsers(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        # await asyncio.sleep(1)
        print(User.objects.filter(is_active=True))
        return HttpResponse("Hello World!")
