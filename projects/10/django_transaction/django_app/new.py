import requests


class CustomTest:
    """
    +: Отвязано от Django
    -: csrf, real database, not link to tests
    """

    @staticmethod
    def create_user():
        test_username = "Bogdan_112345"
        # test_username = "hi"
        test_password = "Qwerty!12345"

        response = requests.post(
            "http://127.0.0.1:8000/api/post_create_user/",
            data={
                "username": test_username,
                "password": test_password
            }
        )
        if response.status_code != 200:
            raise Exception("Тест не пройден")
        print("""\n\n\n
                ################################################################################
                ################################################################################
                ################################################################################
                                        ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ
                ################################################################################
                ################################################################################
                ################################################################################
                \n\n\n""")


if __name__ == "__main__":
    CustomTest.create_user()
