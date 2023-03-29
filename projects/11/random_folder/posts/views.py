from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, routers, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Todo
from posts.serializers import UserSerializer, TodoSerializer


def first(request):
    return HttpResponse('hi')


def second(request):
    return JsonResponse({"data": "hi"})


def third(request: HttpRequest) -> JsonResponse:
    user = User.objects.get(id=1)
    user_json = {
        "username": user.username,
        "email": user.email,
    }
    return JsonResponse(data=user_json, safe=False)


@login_required
@api_view(http_method_names=['GET', 'POST'])
def forth(request: Request) -> Response:
    if request.method == "GET":
        user = User.objects.get(id=1)
        user_json = UserSerializer(user, many=False)
        data = user_json.data

        return Response(data=data, status=200)
    elif request.method == "POST" or request.method == "PUT":
        pass
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



class Forth(APIView):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=1)
        user_json = UserSerializer(user, many=False)
        data = user_json.data
        return Response(data=data, status=200)


class UserList(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def patch(self):
        pass
    def put(self):
        pass


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.filter(id=1)
    serializer_class = TodoSerializer



router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('todos', TodoViewSet)
