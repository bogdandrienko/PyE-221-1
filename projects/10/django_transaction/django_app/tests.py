from django.contrib.auth.models import User
from django.test import TestCase, Client
from django_app import models
from django.urls import reverse


# Create your tests here.

"""

# запуск всех тестов
python manage.py test

# Запуск приложения
python manage.py test django_app

# Запуск всего файла tests внутри приложения
python manage.py test django_app.tests

# Запуск класса
python manage.py test django_app.tests.DefaultUserCreateTestCase

# Запуск метода
python manage.py test django_app.tests.DefaultUserCreateTestCase.test_model_create

"""


class DefaultUserCreateTestCase(TestCase):  # создаёт запись не в настоящей базе данных
    def setUp(self) -> None:  # преднастройка перед тестированием
        print("setUp DefaultUserCreateTestCase")
        User.objects.create_user(username="Anya", password="Qwerty!12345")
        # User.objects.create_user(username="Anya1", password="Qwerty!12345")

        # serial (auto_increment)

    def test_model_create(self):
        """
        Тестируем, что модель пользователя в базе данных успешно создалась
        """

        test_name = "Anya"
        user = User.objects.get(username=test_name)
        self.assertEqual(user.username, test_name)

    def test_user_count(self):
        users = User.objects.all()
        print(users)
        self.assertEqual(users.count(), 1)


class ApiBookGetTestCase(TestCase):
    def setUp(self) -> None:  # преднастройка перед тестированием
        print("\nsetUp ApiBookGetTestCase")
        models.Book.objects.create(title="Tom Soyer 2")

    def test_model_create(self):
        """
        Тестируем, что получение данных с django MVT (JsonResponse)
        """

        client = Client()  # requests
        response = client.get(reverse("get_all_books"))
        print(response.body)
        self.assertEqual(response.status_code, 200)
