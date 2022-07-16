import multiprocessing
import threading
import time
import asyncio
import requests
import aiohttp


def data_analyse(func):
    def obertka(*args, **kwargs):
        print(args)  # ('Bogdan', 'Saadat')
        print(type(args))
        print(kwargs)  # {'author': 'Bogdan', 'name': 'Saadat'}
        print(type(kwargs))

        kwargs["author"] = kwargs["author"] + " !!!"

        result = func(*args, **kwargs)

        post_result = (result, len(result))  # кортеж из двух элементов, где второй это длина массива

        return post_result

    return obertka


@data_analyse
def get_data(name: str, author):
    return f"Hello {name}, {author}"


val1 = ('Bogdan', 'Saadat')
val2 = {'author': 'Bogdan', 'name': 'Saadat'}


# data = get_data(**val2)
# print(data)

# url = 'https://www.gismeteo.kz/weather-zhetikara-11043/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/102.0.0.0 Safari/537.36'}
#
# res = requests.get(
#     url=url,
#     headers=headers
# )
# # print(res)
# # print(type(res))
# #
# # print(res.status_code)
# # print(type(res.status_code))
# #
# # print(res.content)
# # print(type(res.content))
#
# data = res.text
# # print(data)
# # print(type(data))
#
# data1 = data.split('''class="weathertabs day-1"''')[1]
# # print(data1)
# # print(type(data1))
# # print(len(data1))
#
# data2 = data1.split('''Сейчас''')[1].split('''Завтра''')[0].split('''class="unit unit_temperature_c">''')
# print(data2)
# print(type(data2))
# print(len(data2))
#
# # for i in data2:
# #     print(i, '\n\n')
#
# data3 = data2[-2::1]  # [шаг:стоп:шаг] [::] - [идём с нулевого:до последнего:1]
# print(data3)
# print(type(data3))
# print(len(data3))
#
# day = ''
# night = ''
#
# for i in data3:
#     if len(data3[1]) == len(i):
#         day = i.split('''</span>''')[0]
#     else:
#         night = i.split('''</span>''')[0]
# print(f'''темпаратура днём: {day}, а ночью: {night}, город: {'https://www.gismeteo.kz/weather-zhetikara-11043/'.split('weather-')[1].split('-')[0]}''')
#

class Response:
    def __init__(self):
        content, code = self.validate()
        self.status_code = code
        self.content = content
        self.text = b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b'.decode()

    def validate(self):
        result = (b'\xd0\x91\xd0\xb0\xd0\xb9\xd1\x82\xd1\x8b', 200)
        return result


# res1 = Response()
# print(res1)
# print(type(res1))
#
# print(res1.status_code)
# print(type(res1.status_code))
#
# print(res1.content)
# print(type(res1.content))
#
# print(res1.text)
# print(type(res1.text))

# print("Тлеген".encode().decode())


def time_zamer(func):
    def obertka(*args, **kwargs):
        time_start = time.perf_counter_ns()

        result = func(*args, **kwargs)

        time_stop = time.perf_counter_ns()

        print((time_stop - time_start) // 1000000, 'ms')  # 1 424 236 700   - -9 -6 -3

        return result

    return obertka


def get_meteo(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/102.0.0.0 Safari/537.36'}
    res = requests.get(
        url=url,
        headers=headers
    )
    data1 = res.text.split('''class="weathertabs day-1"''')[1]
    data2 = data1.split('''Сейчас''')[1].split('''Завтра''')[0].split('''class="unit unit_temperature_c">''')
    data3 = data2[-2::1]
    day = ''
    night = ''
    for i in data3:
        if len(data3[1]) == len(i):
            day = i.split('''</span>''')[0]
        else:
            night = i.split('''</span>''')[0]
    print(f'''темпаратура днём: {day}, а ночью: {night}, город: {url.split('weather-')[1].split('-')[0]}''')


city_list = [
    'https://www.gismeteo.kz/weather-zhetikara-11043/',
    'https://www.gismeteo.kz/weather-kostanay-4628/',
    'https://www.gismeteo.kz/weather-shymkent-5324/',
    'https://www.gismeteo.kz/weather-nur-sultan-5164/',
    'https://www.gismeteo.kz/weather-almaty-5205/',
    'https://www.gismeteo.kz/weather-zhetikara-11043/',
    'https://www.gismeteo.kz/weather-kostanay-4628/',
    'https://www.gismeteo.kz/weather-shymkent-5324/'
]


@time_zamer
def sync():  # 1 поток, 1 процесс
    for city in city_list:
        get_meteo(url=city)


@time_zamer
def thread():  # несколько потоков, 1 процесс
    # thread1 = threading.Thread(target=get_meteo, args=('https://www.gismeteo.kz/weather-zhetikara-11043/',))
    # thread1.start()
    # thread1.join()

    thread_list = []
    for city in city_list:
        new_thread = threading.Thread(target=get_meteo, args=(city,))
        thread_list.append(new_thread)

    # print(thread_list)
    # print(type(thread_list[0]))

    for new_thread in thread_list:
        new_thread.start()

    for new_thread in thread_list:
        new_thread.join()


@time_zamer
def process():  # 1 поток, несколько процессов
    # name1 = multiprocessing.Process(target=get_meteo, args=('https://www.gismeteo.kz/weather-zhetikara-11043/',))
    # name1.start()
    # name1.join()

    thread_list = []
    for city in city_list:
        new_thread = multiprocessing.Process(target=get_meteo, args=(city,))
        thread_list.append(new_thread)

    # print(thread_list)
    # print(type(thread_list[0]))

    for new_thread in thread_list:
        new_thread.start()

    for new_thread in thread_list:
        new_thread.join()


async def async_get_meteo(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/102.0.0.0 Safari/537.36'}
    async with aiohttp.ClientSession() as ses:
        async with ses.get(
                url=url,
                headers=headers
        ) as response:
            res = await response.read()

    data1 = res.decode().split('''class="weathertabs day-1"''')[1]
    data2 = data1.split('''Сейчас''')[1].split('''Завтра''')[0].split('''class="unit unit_temperature_c">''')
    data3 = data2[-2::1]
    day = ''
    night = ''
    for i in data3:
        if len(data3[1]) == len(i):
            day = i.split('''</span>''')[0]
        else:
            night = i.split('''</span>''')[0]
    print(f'''темпаратура днём: {day}, а ночью: {night}, город: {url.split('weather-')[1].split('-')[0]}''')


@time_zamer
def async_func():  # 1 поток, 1 процесс
    # for city in city_list:
    #     get_meteo(url=city)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(
            *[async_get_meteo(city) for city in city_list]
        )
    )


if __name__ == '__main__':
    sync()  # 1950 ms         -> 0 ms
    # thread()  # 301 ms        -> 1 ms
    # process()  # 577 ms       -> 262 ms (0,25 s)
    # async_func()  # 248 ms      -> 0 ms
    pass
