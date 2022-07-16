import time
import requests
import threadi
import multiprocessing
import asyncio
import aiohttp

# import new
# from api.main import index
from new import Example

print(Example.get_round(10.66))


# print(new.func_1())

# print(func_1())

def measure(func):
    def wrap(*args, **kwargs):
        print('start measure')

        time1 = time.perf_counter()
        res = func(*args, **kwargs)  # ядро декорируемой функции

        print('end measure')
        print(f'функция потратила времени: {time.perf_counter() - time1}')
        return res

    return wrap


def download_image(name):
    response = requests.get(
        url="https://picsum.photos/370/250",
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
    )

    # print(response)
    # print(type(response))

    #  response.status_code  # 200
    #  response.content  # bytes b""

    with open(f'temp/image_{name}.jpg', 'wb') as file:
        file.write(response.content)


@measure
def sync_f():
    for i in range(1, 100):
        download_image(i)


@measure
def threading_f():
    # thread_1 = threading.Thread(
    #     target=download_image,
    #     args=("thread_1",),
    #     kwargs={}
    # )
    #
    # thread_1.start()
    # thread_1.join()

    thread_list = [threading.Thread(target=download_image, args=(f"thread_{x}",), kwargs={}) for x in range(1, 100)]

    # thread_list = []
    # for x in range(1, 10):
    #     thread_list.append(threading.Thread(target=download_image, args=(f"thread_{x}",), kwargs={}))

    for i in thread_list:
        i.start()

    for i in thread_list:
        i.join()

    # exit


@measure
def processing_f():
    # process_1 = multiprocessing.Process(
    #     target=download_image,
    #     args=("process_1",),
    #     kwargs={}
    # )
    #
    # process_1.start()
    # process_1.join()

    process_list = [multiprocessing.Process(target=download_image, args=(f"process_{x}",), kwargs={}) for x in
                    range(1, 100)]

    for i in process_list:
        i.start()

    for i in process_list:
        i.join()

    # exit


async def async_download_image(name):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/102.0.0.0 Safari/537.36'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://picsum.photos/370/250", headers=headers) as await_response:
            data = await await_response.read()

    with open(f'temp/image_{name}.jpg', 'wb') as file:
        file.write(data)


@measure
def async_f():
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(async_download_image("async_1"))

    async def tasks_generator():  # корутины - coro  - задачи с задержкой по выполнению и возврату
        await asyncio.gather(
            *[async_download_image(f"async_{x}") for x in range(1, 100)]
        )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks_generator())


def tick(name):
    print(f'tick {name} start\n')
    time.sleep(1.0)
    print(f'tick {name} end\n')


async def tick_a(name):
    print(f'tick {name} start\n')
    await asyncio.sleep(1)
    print(f'tick {name} end\n')


@measure
def start():
    # последовательно
    # tick("sync 1")
    # tick("sync 2")
    # tick("sync 3")

    # thread_1 = threading.Thread(target=tick, args=("thread 1",))
    # thread_1.start()
    #
    # thread_2 = threading.Thread(target=tick, args=("thread 2",))
    # thread_2.start()
    #
    # thread_3 = threading.Thread(target=tick, args=("thread 3",))
    # thread_3.start()
    #
    # thread_1.join()
    # thread_2.join()
    # thread_3.join()

    # process_1 = multiprocessing.Process(target=tick, args=("process 1",))
    # process_1.start()
    #
    # process_2 = multiprocessing.Process(target=tick, args=("process 2",))
    # process_2.start()
    #
    # process_3 = multiprocessing.Process(target=tick, args=("process 3",))
    # process_3.start()
    #
    # process_1.join()
    # process_2.join()
    # process_3.join()

    async def tasks_generator():  # корутины - coro  - задачи с задержкой по выполнению и возврату
        await asyncio.gather(
            *[tick_a(f"async_{x}") for x in range(1, 4)]
        )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks_generator())


if __name__ == '__main__':  # точка входа, т.е. отсюда стартует этот файл при запуске
    # sync_f()  # 59.278442899999995       1 thread * 1 process
    # threading_f()  # 3.6611930999999998  1 * 100
    # processing_f()  # 4.1108648          100 * 1
    # async_f()  # 2.7549684                 1 * 1
    start()
# последовательно - 1 поток, 1 процесс (по очереди)
# многопоточно - N поток, 1 процесс
# мультипроцесс - N поток, N процесс
# асинхронно - 1 поток, 1 процесс (цикл событий)
