from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


# Create your views here.

class GetAll:
    def get(self, request):
        objs = Book.objects.all()
        books = objs[len(objs) - 5::]
        return render(request, "booking/read_all_books.html", context={"books": books})

    def post(self, request):
        name = request.POST.get('name')
        obj = Book.objects.create(title=name, description=name, price=666.0, author=name)
        objs = Book.objects.all()
        books = objs[len(objs) - 5::]
        return render(request, "booking/read_all_books.html", context={"books": books})


def read_all_books(request):
    if request.method == "POST":
        name = request.POST.get('name')
        obj = Book.objects.create(title=name, description=name, price=666.0, author=name)
    objs = Book.objects.all()
    books = objs[len(objs) - 5::]
    return render(request, "booking/read_all_books.html", context={"books": books})


def temp_create(request):
    # title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    # upload_author = models.ForeignKey()
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    # description = models.TextField()
    # publication_date = models.DateTimeField(default=timezone.now)
    # for i in range(5, 100):
    #     Book.objects.create(
    #         title=f"title {i}",
    #         author=User.objects.all()[0],
    #         price=0.0,
    #         description=f"description {i}",
    #     )
    # usr = User.objects.all()[0]
    # obj = Book(title='title 0',author=usr, price=0.0, description="description 0")
    # obj.save()

    return HttpResponse("<h1></h1>")
