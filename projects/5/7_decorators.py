from typing import Union


def decor_append_slash_to_request(func):
    def wrapper(url: str):
        # ПРЕДОБРАБОТКА
        print(url.split(sep="/")[-1].find('?') >= 0)
        if not url.split(sep="/")[-1].find('?') >= 0:
            if url[-1] != '/':
                url += "/"
        # ПРЕДОБРАБОТКА

        response = func(url=url)

        # ПОСТОБРАБОТКА
        if response:
            for key, value in response.items():
                response[key] = hash(value)
        print(f"response: {response}")
        # ПОСТОБРАБОТКА

        return response

    # def func(): pass  # - определение функции
    # func()  # - вызов функции
    # func - ссылка на функцию
    return wrapper


@decor_append_slash_to_request
def get_data_from_api(url: str):
    print(f"Тут идёт запрос к базе, {url}")
    print("Тут мы возвращаем данные браузеру")
    return {"admin": "Bogdan", "pswrd": "12345"}


@decor_append_slash_to_request
def get_data_from_api2(url: str):
    print(f"Тут идёт запрос к базе, {url}")
    print("Анализ и изменение данных")
    print("Тут мы возвращаем данные браузеру")
    return None


def get_data_from_api3(url: str):
    # ПРЕДОБРАБОТКА
    print(url.split(sep="/")[-1].find('?') >= 0)
    if not url.split(sep="/")[-1].find('?') >= 0:
        if url[-1] != '/':
            url += "/"

    # ПРЕДОБРАБОТКА

    def get_data_from_api2(url: str):
        print(f"Тут идёт запрос2414124 к базе, {url}")
        print("Анализ и изменение данных")
        print("Тут мы возвращаем данные браузеру")

        return None

    response = get_data_from_api2(url=url)

    # ПОСТОБРАБОТКА
    if response:
        for key, value in response.items():
            response[key] = hash(value)
    print(f"response: {response}")
    # ПОСТОБРАБОТКА

    return response


# result1 = get_data_from_api(url="https://logbook.itstep.org/?name=Python")
# result2 = get_data_from_api2(url="https://logbook.itstep.org")
#
# print(f"result1: {result1}")
# print(f"result2: {result2}")

# Декоратор для проверки регистрации пользователя


# List comprehension

list1 = []
for i in range(1, 100):
    if i % 2 == 0:
        list1.append({f"{i}": 100 - i})
print(list1)

list2 = [{f"{i}": 100 - i} for i in range(1, 100) if i % 2 == 0]
print(list2)


def summary(a, b):
    return a + b


lam1 = lambda a, b: a + b

print(lam1(99, 1))


def recur(start_value: int, stop_value: Union[int, float]) -> Union[int, None]:
    if start_value < stop_value:
        start_value += 1
        print(start_value)
        recur(start_value, stop_value)
    else:
        return start_value


recur(start_value=1, stop_value=10.0)


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


num = 7
print(recur_factorial(num))

# start_value = 0
# stop_value = 10
# while True:
#     if start_value < stop_value:
#         start_value += 1
#         print(start_value)
#     else:
#         break


