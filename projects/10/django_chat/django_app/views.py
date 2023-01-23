from django.http import JsonResponse
from django.shortcuts import render
from django_app import models
from django.contrib.auth.decorators import login_required


def data(request):
    return JsonResponse(data={"data": "Python is awesome!"}, safe=False)

def rooms(request):
    return render(request, "home.html", context={"rooms": models.Room.objects.all()})


@login_required
def room(request, slug):
    room_obj = models.Room.objects.get(slug=slug)
    return render(
        request,
        "room.html",
        context={"room": room_obj, "messages": models.Message.objects.filter(room=room_obj)[:25]}
    )
