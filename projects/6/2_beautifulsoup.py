import asyncio
import concurrent.futures
import multiprocessing
import threading
import time

import requests
import aiohttp
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def get_temp_string(url: str, city_name: str):
    time.sleep(20)

    response1 = requests.get(url=url, headers=headers)
    soup2 = BeautifulSoup(response1.text, 'html.parser')
    objs3 = soup2.find_all('span', {'class': 'unit unit_temperature_c'})
    objs4 = [x.text.strip() for x in objs3]
    print(f"{city_name}: day: {objs4[3]} | night: {objs4[2]}\n")
    return f"{city_name}: day: {objs4[3]} | night: {objs4[2]}"


def write_image_from_url(image_name: str) -> None:
    with open(f'images/{image_name}.jpg', mode='wb') as file:
        file.write(requests.get(url='https://picsum.photos/600/600/', headers=headers).content)


def sync_download_image():
    for i in range(1, 10 + 1):
        write_image_from_url(image_name=f'img{i}')


def multithread_download_image():
    # tasks = []
    # for x in range(1, 10+1):
    #     tasks.append(threading.Thread(target=write_image_from_url, kwargs={"image_name": f'img{x}'}))
    # for task in tasks:
    #     task.start()
    # for task in tasks:
    #     task.join()

    current_thread = 16
    with concurrent.futures.ThreadPoolExecutor(max_workers=current_thread * 2 + 1) as executor:
        for x in range(1, 10 + 1):
            executor.submit(write_image_from_url, f'img{x}')


def multiprocess_download_image():
    # tasks = []
    # for x in range(1, 10 + 1):
    #     tasks.append(multiprocessing.Process(target=write_image_from_url, kwargs={"image_name": f'img{x}'}))
    # for task in tasks:
    #     task.start()
    # for task in tasks:
    #     task.join()

    current_thread = 16
    with concurrent.futures.ProcessPoolExecutor(max_workers=current_thread * 2 + 1) as executor:
        for x in range(1, 10 + 1):
            executor.submit(write_image_from_url, f'img{x}')


async def as_write_image_from_url(image_name: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get('https://picsum.photos/600/600/') as clien_response:
            response = await clien_response.read()

    with open(f'images/{image_name}.jpg', mode='wb') as file:
        file.write(response)


async def async_download():
    await asyncio.gather(*[as_write_image_from_url(f'img{i}') for i in range(1, 10 + 1)])


def async_download_image():
    asyncio.run(async_download())


def threadings():
    citys = [
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/', "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-nur-sultan-5164/', "city_name": "nur-sultan"},
        {"url": 'https://www.gismeteo.kz/weather-almaty-5205/',
         "city_name": "almaty"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-nur-sultan-5164/',
         "city_name": "nur-sultan"},
        {"url": 'https://www.gismeteo.kz/weather-almaty-5205/',
         "city_name": "almaty"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-nur-sultan-5164/',
         "city_name": "nur-sultan"},
        {"url": 'https://www.gismeteo.kz/weather-almaty-5205/',
         "city_name": "almaty"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
        {"url": 'https://www.gismeteo.kz/weather-nur-sultan-5164/',
         "city_name": "nur-sultan"},
        {"url": 'https://www.gismeteo.kz/weather-almaty-5205/',
         "city_name": "almaty"},
        {"url": 'https://www.gismeteo.kz/weather-shymkent-5324/',
         "city_name": "shymkent"},
    ]

    # for city in citys:
    #     get_temp_string(url=city["url"], city_name=city.get("city_name"))

    # citys_tasks = []
    # for city in citys:
    #     new_thread = threading.Thread(
    #         target=get_temp_string, kwargs={
    #             "url": city.get("url"),
    #             "city_name": city.get("city_name")
    #         }
    #     )
    #     citys_tasks.append(new_thread)
    #
    # for task in citys_tasks:
    #     task.start()
    #
    # for task in citys_tasks:
    #     task.join()
    # current_thread = 8
    #
    # with concurrent.futures.ThreadPoolExecutor(max_workers=current_thread * 2 + 1) as executor:
    #     for city in citys:
    #         future = executor.submit(get_temp_string, city.get("url"), city.get("city_name"))
    #         # result = future.result()

    # with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
    #     for city in citys:
    #         future = executor.submit(get_temp_string, city.get("url"), city.get("city_name"))
    #         # result = future.result()


if __name__ == "__main__":
    time1 = time.perf_counter()

    # threadings()
    # sync_download_image()  # 7.3
    # multithread_download_image()  # 0.9 | 1.0
    # multiprocess_download_image()  # 1.5 | 1.7
    async_download_image()  # 1.3

    print(round(time.perf_counter() - time1, 1))

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# response = requests.get(url="", headers=headers)
# # print(response.text)
# soup = BeautifulSoup(response.text, 'html.parser')
# objs = soup.find_all('span', {'class': 'unit unit_temperature_c'})
# objs2 = [x.text.strip() for x in objs]
# print(f"Нур-Султан: day: {objs2[3]} | night: {objs2[2]}")
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
# response = requests.get(url="", headers=headers)
# # print(response.text)
# soup = BeautifulSoup(response.text, 'html.parser')
# objs = soup.find_all('span', {'class': 'unit unit_temperature_c'})
# objs2 = [x.text.strip() for x in objs]
# print(f"Алматы: day: {objs2[3]} | night: {objs2[2]}")
