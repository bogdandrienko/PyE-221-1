import time

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.views import View
from django.views.decorators.cache import cache_page
from django.core.cache import caches

DatabaseCache = caches["default"]
LocMemCache = caches["special"]
RedisCache = caches["extra"]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


class UserListView(View):
    def get(self, *args, **kwargs):
        time_start = time.perf_counter()

        # for i in range(1, 1000):
        #     User.objects.create(
        #         username=f"user_{i}",
        #         password=make_password(f"user_{i}")
        #     )

        # TODO 1 execute ########################
        # import psycopg2
        # connection = psycopg2.connect("...")
        # cursor = connection.cursor()
        # cursor.execute("select username from users;")

        caches_res = "Кэша не было"
        users = LocMemCache.get("users_UserListView")
        if users is None:
            caches_res = "Кэша не был"
            users = User.objects.all()  # ORM < clear SQL [speed]
            LocMemCache.set("users_UserListView", users, timeout=60*1)

        # TODO 1 execute ########################

        # TODO 2 serialize ########################
        # users = [{"username": x.username} for x in users]  # O(1) > O(n) > O(log())
        # users = ({"username": x.username} for x in users)  # O(1) > O(n) > O(log())
        # TODO 2 serialize ########################

        # elem1 = 6
        # list1 = [1, 2, 3, 4, 3, 4, 5, 6, 7]  # 1ms O(n)
        # for i in list1:
        #     if elem1 == i:
        #         print("FIND")
        #
        # dict1 = {"key1": "value1", "key2": "value1", "key3": "value1"}  # O(1)

        time_end = time.perf_counter()
        return JsonResponse(data={"result": round(time_end-time_start, 9), "res": caches_res}, safe=False)
    def post(self, *args, **kwargs):
        users = User.objects.all()
        users = [{"username": x.username} for x in users]
        return JsonResponse(data=users, safe=False)


def usr(request):
    time_start = time.perf_counter()

    caches_res = ""
    caches_res = "Cache find"
    users = RedisCache.get("hotNews")
    if users is None:
        caches_res = "Cache not found"
        users = User.objects.all()
        RedisCache.set("hotNews", users, timeout=5)
    # users = User.objects.all()
    # for i in users:
    #     print(i.username)

    time_end = time.perf_counter()
    return JsonResponse(data={"result": round(time_end-time_start, 6), "res": caches_res}, safe=False)


@cache_page(60 * 5)
def weather(request):
    response = requests.get("https://www.gismeteo.kz/weather-almaty-5205/", headers=headers)
    # response = requests.get("https://www.gismeteo.kz/weather-lagos-6834/", headers=headers)
    text = response.text  # response.content.decode(encoding="utf-8")

    sep1 = 'Завтра</div><div class="tab-temp tab-charts">'
    text1 = text.split(sep=sep1)[0]

    sep2 = '<div class="day">Сегодня</div><div class="tab-temp tab-charts">'
    text2 = text1.split(sep=sep2)[1]

    sep3 = 'unit unit_temperature_c">'
    text3 = text2.split(sep=sep3)[-2::]

    sep4 = '</span>'
    weather_arr = []
    for i in text3:
        txt1 = i.split(sep=sep4)
        txt2 = txt1[0]
        txt3 = txt2.replace("&minus;", "-")
        weather_arr.append(txt3)
    result = {"day": f"{weather_arr[1]}", "night": f"{weather_arr[0]}"}
    return render(request, "weather.html", context={"result": result})


def currency(request, mul: str):
    response = requests.get("https://finance.rambler.ru/calculators/converter/1-KZT-USD/", headers=headers)
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    result = int(mul) * round(float(soup.find_all('div', class_="converter-display__value")[-1].get_text()), 2)
    return render(request, "currency.html", context={"result": result})
