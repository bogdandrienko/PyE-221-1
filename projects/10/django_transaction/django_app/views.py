import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from django.db import transaction
from django_app import models
import re

# Create your views here.

# Несколько операций, связанных между собой, должны выполнятся в рамках транзакции,
# т.к. даже успешное выполнение первых, но отказ последующих должно вызывать откат изменений:
# перевод средств другому человеку.

"""
SELECT * FROM public.products
ORDER BY id ASC 


BEGIN TRANSACTION;
insert into public.products (title, price, count, type_measure, nomeklatura_id) values ('новый', '666', '10', 'kg', 'новый_2')

BEGIN;
insert into public.products (title, price, count, type_measure, nomeklatura_id) values ('новый', '666', '10', 'kg', 'новый_2')
--COMMIT TRANSACTION;
--ROLLBACK TRANSACTION;

BEGIN TRANSACTION;
delete from public.products; 


do
$$
BEGIN 
	insert into public.products (title, price, count, type_measure, nomeklatura_id) values ('новый', '666', '10', 'kg', 'новый_2');
	commit;
EXCEPTION WHEN OTHERS
THEN
	rollback;
    --raise exception 'Такая строка уже есть!';
END;
$$
language plpgsql;
"""


@transaction.atomic
# @transaction.non_atomic_requests
def delete_users(request):
    pass


def create_users(request: HttpRequest) -> HttpResponse:
    try:
        # todo START TRANSACTION
        transaction.set_autocommit(False)  # todo ! django default = autocommit = TRUE !
        user = User.objects.create(username="Alice", password=make_password("Alice123"))
        # todo danger action ###############################################################
        # profile = UserProfile.objects.create(user=user, fio="fio")
        # account = UserToken.objects.create(user=user, fio="fio")
        # if user and profile and account:
        #     return "success"
        # else:
        #     raise Exception("error!")
        # print(1 / 0)
        # todo danger action ###############################################################
        transaction.commit()  # применение изменений в базе после начала транзакции
        return HttpResponse("<h1>Пользователь успешно создан!</h1>")
    except Exception as error:
        print(f"[ERROR] ({datetime.datetime.now()}): ", error)
        transaction.rollback()  # откатить все изменения в базе после начала транзакции
        return HttpResponse(f"<h1>Ошибка создания {error}</h1>")


def create_users_points(request: HttpRequest) -> HttpResponse:
    transaction.set_autocommit(False)
    transaction_id = transaction.savepoint()  # точка сохранения 1
    try:
        # user = User.objects.create_user(username="Alice", password="Alice123")
        user = User.objects.create(username="Alice", password=make_password("Alice123"))

        if user is not None:
            transaction.savepoint_commit(transaction_id)  # применение точка сохранения 1

            transaction_id = transaction.savepoint()  # точка сохранения 2
            res = 10 - 0  # profile = UserProfile.objects.create(user=user, fio="fio")
            if res < 0:
                transaction.savepoint_commit(transaction_id)  # применение точка сохранения 2
            else:
                transaction.savepoint_rollback(transaction_id)  # откат точка сохранения 2
        else:
            transaction.savepoint_rollback(transaction_id)  # откат точка сохранения 1

    except Exception as error:
        print(f"[ERROR] ({datetime.datetime.now()}): ", error)
        transaction.savepoint_rollback(transaction_id)

        return HttpResponse(f"<h1>Ошибка создания {error}</h1>")
    else:
        transaction.savepoint_commit(transaction_id)

        return HttpResponse("<h1>Пользователь успешно создан!</h1>")


def check(request):
    def create():
        # todo CREATE ####################################################################

        # single create
        f"""
        insert into public.django_app_book (title) values ('Война и мир')
        """
        # obj = models.Book.objects.create(title="Война и мир")
        # print(obj)
        # single create

        # mass create
        f"""
        insert into public.django_app_book (title) values ('Война и мир'), ('Война и мир'), ('Война и мир')
        """

        # for i in ('Война и мир', 'Война и мир', 'Война и мир'):  # todo too many requests!
        #     models.Book.objects.create(title=i)

        # file = open("new.txt", "w")
        # try:
        #     file.write("hello")
        #
        #     # только если не было исключений
        #     # commit()
        # except Exception as error:
        #     pass
        # else:
        #     # только если не было исключений
        #     # commit()
        #     pass
        # finally:
        #     file.close()

        # with open("new.txt", "w") as file:
        #     file.write("hello")

        # list1 = []
        # for i in range(1, 1000):
        #     if i % 2 == 0:
        #         list1.append({"name": i, "age": i ** 2})
        # print(list1)
        #
        # print([{"name": i, "age": i ** 2} for i in range(1, 1000) if i % 2 == 0])

        # class People(object):
        #     def __init__(self, title):
        #         self.title = title

        # list_objects_for_create = []
        # for i in ('Война и мир', 'Война и мир', 'Война и мир'):
        #     pep1 = models.Book(title=i)
        #     list_objects_for_create.append(pep1)
        # models.Book.objects.bulk_create(list_objects_for_create)
        #
        models.Book.objects.bulk_create([
            models.Book(title=x)
            for x in ('Война и мир', 'Война и мир', 'Война и мир')
        ], batch_size=1000)
        # mass create

        # todo CREATE ####################################################################

    def read():
        # todo READ ####################################################################

        # single read
        """
        select id, title from public.django_app_book where id='24';
        """

        # book = models.Book.objects.get(id=24)
        # print(book)

        # single read

        # mass read

        # rows = [("id", "title", 'name', "description"), ("id", "title", 'name', "description")]
        # print(rows[0][2])
        # book = books[0]
        # book.title
        # book.id
        # mass read

        """
        select * from public.django_app_book;
        select * from public.django_app_book where title='Война и мир';
        
        select * from public.django_app_book ORDER BY id DESC, title ASC;
        select * from public.django_app_book WHERE R <= 2;
        select id, title from public.django_app_book WHERE R <= 2;
        select * from public.django_app_book WHERE id > 2;
        select * from public.django_app_book WHERE id = 2;
        SELECT ... WHERE headline ILIKE '%Lennon%';
        SELECT ... WHERE headline LIKE 'Lennon%';
        SELECT ... WHERE headline LIKE '%Lennon';
        """

        # https://docs.djangoproject.com/en/4.1/ref/models/querysets/

        # books = models.Book.objects.all()
        # books = models.Book.objects.filter(title='Война и мир')
        # books = models.Book.objects.order_by('-id', 'title')
        # books = models.Book.objects.all()[:2]
        # books = models.Book.objects.only("id", "title")
        # books = models.Book.objects.filter(id__gte=2, id__le=10) # greater than
        # books = models.Book.objects.filter(id__eq=2) # equal
        # Entry.objects.get(headline__icontains='Lennon') WithLennon
        # Entry.objects.filter(headline__startswith='Lennon') WithLennon
        Entry.objects.filter(headline__endswith='Lennon')
        # print(books)

        # todo READ ####################################################################

    def update():
        # todo UPDATE ####################################################################

        # single update
        """
        UPDATE public.django_app_book SET title = title || '_обновление' where id='24';
        """
        # book = models.Book.objects.get(id=24)
        # print(book)
        # book.title = book.title + '_обновление'
        # book.save()
        # single update

        # mass update
        """
        UPDATE public.django_app_book SET title = title || '_новое поступление' where title='Война и мир';
        """

        # books = models.Book.objects.filter(title='Война и мир_новое поступление')
        # print(books)
        # for i in books:
        #     i.title = i.title.split("_")[0] + "_уже устарело"
        #     i.save()

        # models.Book.objects.bulk_update([
        #     models.Book(title=x)
        #     for x in ('Война и мир', 'Война и мир', 'Война и мир')
        # ], batch_size=1000)
        # mass update

        # todo UPDATE ####################################################################

    def delete():
        # todo DELETE ####################################################################
        # single delete
        f"""
        delete from public.django_app_book where id='1'
        """
        models.Book.objects.get(id=1).delete()  # ! todo not unique
        # single delete

        # mass delete
        f"""
        delete from public.django_app_book where title='Война и мир'
        """
        # obj = models.Book.objects.all().filter(title="Война и мир")
        models.Book.objects.filter(title="Война и мир").delete()
        # mass delete

        # todo DELETE ####################################################################

    update()

    return HttpResponse("<h1>Успешно создано!</h1>")


# хэширование - одностронне - нельзя повернуть вспять (hash, hashlib, dictionary O(1) - константное)
# O(log(n)) - логарифмический
# O(N) - линейная сложность, цикл одномерный

# шифрование - двухстороння - ecrypt(source, key) -> shifr | decrypt(shifr, key) -> source


def get_public_all_books(request):
    if request.method == "GET":
        return JsonResponse(data=None, safe=False, status=200)
        # if request.user.is_authenticated:
        books = [{"id": i.id, "title": i.title} for i in models.Book.objects.all() if i.id % 2 == 0]
        return JsonResponse(data=books, safe=False)
        # else:
        #     return JsonResponse(data=None, safe=False, status=401)
    raise Exception("Method Not Allowed")


def get_private_all_books(request):
    if request.method == "GET":
        return JsonResponse(data=None, safe=False, status=200)
        # if request.user.is_authenticated:
        books = [{"id": i.id, "title": i.title} for i in models.Book.objects.all()]
        return JsonResponse(data=books, safe=False)
        # else:
        #     return JsonResponse(data=None, safe=False, status=401)
    raise Exception("Method Not Allowed")


@csrf_exempt
def post_create_user(request):
    try:
        # Trip              # Trip | Trip* | *Trip | *Trip*
        # TripVehicle       # Trip* | *Trip*
        # DataTripVehicle   # *Trip*
        # Data_Trip         # *Trip | *Trip*

        # Trip*
        # *.jp*g | *.xlsx

        username = request.POST["username"]
        password = request.POST["password"]

        if not re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[_-])(?=.*?[0-9]).{8,}$", username):
            print("Имя пользователя не соответствует уровню")
            return JsonResponse(data={"detail": "Имя пользователя не соответствует уровню"}, safe=False, status=500)
        if not re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[#?!$%^&*-])(?=.*?[0-9]).{12,}$", password):
            print("Пароль не соответствует уровню")
            return JsonResponse(data={"detail": "Пароль не соответствует уровню"}, safe=False, status=500)

        User.objects.create_user(username=username, password=password)
    except Exception as error:
        print(error)
        return JsonResponse(data={"detail": f"{error}"}, safe=False, status=500)
    else:
        return JsonResponse(data={"detail": "success"}, safe=False, status=200)
