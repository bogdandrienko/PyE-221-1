import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.

def index(request):
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


