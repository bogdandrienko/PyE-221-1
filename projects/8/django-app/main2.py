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


if __name__ == '__main__':
    # mass_load_image() # 11.60596
    # mass_load_image_threads()  # 1.16204
    # mass_load_image_process()  # 1.41249
    start = time.perf_counter()

    try:
        asyncio.run(mass_load_image_async())
    except Exception as error:
        pass

    stop = time.perf_counter()
    print(f"заняло времени: {round(stop - start, 5)}")
    pass
