import random
import time

import threading
import multiprocessing
import concurrent.futures
import asyncio

import requests
import aiohttp

# multithreading

# GIL - global intrepreter lock

# url = "https://via.placeholder.com/600/92c952/"  # .png
url = "https://picsum.photos/1920/1080/"  # .png
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def download_image():
    data = requests.get(url=url, headers=headers)
    # print(data.content)
    # print(data)
    # print(data.status_code)
    # print(len(data.content))  # 384 кб
    with open(f'temp/image{random.randint(1, 1000000)}.jpg', 'wb') as open_file:
        open_file.write(data.content)


async def download_image_async():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response_instance:
            data = await response_instance.read()
            with open(f'temp/image{random.randint(1, 1000000)}.jpg', 'wb') as open_file:
                open_file.write(data)


def mass_load_image():
    start = time.perf_counter()
    for i in range(1, 10 + 1):
        download_image()
    stop = time.perf_counter()
    print(f"заняло времени: {round(stop - start, 5)}")


def mass_load_image_threads():  #
    start = time.perf_counter()
    new_theads = []
    optimal_workers = int(16 * 32 // 16)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(1, 10 + 1):
            executor.submit(download_image)

    for i in range(1, 10 + 1):
        new_thead = threading.Thread(target=download_image)
        new_theads.append(new_thead)
    # for i in new_theads:
    #     i.start()
    # for i in new_theads:
    #     i.join()  # заставляет основной поток ждать завершения этого потока

    stop = time.perf_counter()
    print(f"заняло времени: {round(stop - start, 5)}")


def mass_load_image_process():
    start = time.perf_counter()
    new_processes = []

    optimal_workers = int(4)
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        for i in range(1, 10 + 1):
            executor.submit(download_image)

    for i in range(1, 10 + 1):
        new_process = multiprocessing.Process(target=download_image)
        new_processes.append(new_process)
    for i in new_processes:
        i.start()
    for i in new_processes:
        i.join()

    stop = time.perf_counter()
    print(f"заняло времени: {round(stop - start, 5)}")


async def mass_load_image_async():
    await asyncio.gather(*[download_image() for i in range(1, 10 + 1)])  # распаковка корутин из list compreh...


def iterator():
    # объект может выполняет повторения .next()
    # mylist = [1, 2, 3]
    # for i in mylist:
    #     print(i)
    #
    # mylist = [x for x in range(1, 3+1)]  # [1, 2, 3]  # выражение создающее list - list comprehension
    # mydict = {value: key for (key, value) in {"key": "value"}.items()}  # выражение создающее list - list comprehension

    # dict2 = {"v": "k"}
    # print(dict2)  # {'v': 'k'}
    # dict2["key1"] = 12
    # print(dict2)  # {'v': 'k', 'key1': 12}
    # del dict2["v"]
    # print(dict2)  # {'key1': 12}

    # генератор - итератор, но прочитать можно только 1 раз, они не хранят в памяти объекты
    # они их вычисляют на лету
    # mygenerator = (x for x in range(1, 3 + 1))  # genexpr <generator object iterator.<locals>.<genexpr> at 0x000002243125AA40>
    # print(mygenerator)
    # for i in mygenerator:
    #     print(i)

    # def create_gen(val: int):
    #     yield val * val  # return - сложное и дорогое вычисление - lazy computing

    # mylist = range(5, 8+1)
    # for j in mylist:
    #     yield j

    # if True:
    #     gen1 = create_gen(5)  # <generator object iterator.<locals>.create_gen at 0x000001FD710FAA40>
    #     print(gen1)
    #     for i in gen1:
    #         print(i)
    # else:
    #     pass

    # корутина
    async def count():
        print("Начало отсчёта")
        await asyncio.sleep(0)
        print("Промежуток отсчёта")
        await asyncio.sleep(0)
        print("Конец отсчёта")

    # coro1 = count()
    # print(coro1)  # <coroutine object iterator.<locals>.count at 0x00000260D486AA40>
    # coro1.send(None)  # до следующего await - Начало отсчёта
    # coro1.send(None)  # до следующего await - Промежуток отсчёта
    # coro1.send(None)  # до следующего await - Конец отсчёта

    # asyncio.run(count())


if __name__ == '__main__':
    # mass_load_image() # 11.60596
    # mass_load_image_threads()  # 1.16204
    # mass_load_image_process()  # 1.41249
    # start = time.perf_counter()
    #
    # try:
    #     asyncio.run(mass_load_image_async())
    # except Exception as error:
    #     pass
    #
    # stop = time.perf_counter()
    # print(f"заняло времени: {round(stop - start, 5)}")

    iterator()
    pass
