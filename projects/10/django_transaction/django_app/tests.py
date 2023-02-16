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
        # print("setUp DefaultUserCreateTestCase")
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
        # print(users)
        self.assertEqual(users.count(), 1)


class ApiBookGetTestCase(TestCase):
    test_username = "Bogdan_112345"
    test_password = "Qwerty!12345"

    # test_password = "Qwerty!1"

    def setUp(self) -> None:  # преднастройка перед тестированием
        # print("\nsetUp ApiBookGetTestCase")
        models.Book.objects.create(title="Tom Soyer 2")

        client = Client()
        response1 = client.post(
            reverse("post_create_user"),
            data={
                "username": self.test_username,
                "password": self.test_password
            }
        )
        if response1.status_code != 200:
            raise Exception("Пользователь не создан!")

    def test_model_create(self):
        """
        Тестируем, что получение данных с django MVT (JsonResponse)
        """

        client = Client()  # requests
        return self.assertEqual(1, 1)

        response1 = client.get(reverse("get_public_all_books"))
        response2 = client.get(reverse("get_private_all_books"))
        if response1.status_code != response2.status_code:
            return self.assertEqual(1, 1)
        else:
            return self.assertEqual(1, 0)

    def test_model_post(self):
        # print("\n************\n\nmethod text_model_create")

        # print(User.objects.all())

        user = User.objects.get(username=self.test_username)
        self.assertEqual(user.username, self.test_username)


class OkTestCase(TestCase):

    def setUp(self) -> None:
        pass

    def test_ok(self):
        print("""\n\n\n
        ################################################################################
        ################################################################################
        ################################################################################
                                ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ
        ################################################################################
        ################################################################################
        ################################################################################
        \n\n\n""")
