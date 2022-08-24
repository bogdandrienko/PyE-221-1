import time
import threading
import multiprocessing
import asyncio


def decor(func):
    def decor_inline(*args, **kwargs):  # *(12, 15, 6,) - tuple(кортеж) \ **{"name":"Py", 'age': 12} - dict(словарь)
        # ПРЕДОБРАБОТКА
        time_start = time.perf_counter()
        # ПРЕДОБРАБОТКА

        # arg1 = args[1]

        result = func(*args, **kwargs)

        # ПОСТОБРАБОТКА
        print(f'всё действие заняло: {round(time.perf_counter() - time_start, 5)}')
        # ПОСТОБРАБОТКА

        return result

    return decor_inline


def task(name: str) -> None:
    print(f'начало {name}')
    time.sleep(1.0)  # блокирующая операция - обращение в базу данных, загрузка картинки...
    print(f'конец {name}')


async def task_a(name: str) -> None:
    print(f'начало {name}')
    await asyncio.sleep(1.0)  # блокирующая операция - обращение в базу данных, загрузка картинки...
    print(f'конец {name}')


# последовательная
@decor
def synhronus():  # 3.01685
    task(name='Задача 1')
    task(name='Задача 2')
    task(name='Задача 3')


# многопоточность
@decor
def threadings():  # 1.01568

    def task_new():
        new_thread_1 = threading.Thread(target=task, args=('Задача 1',))
        new_thread_1.start()
        new_thread_1.join()

        new_thread_2 = threading.Thread(target=task, args=('Задача 2',))
        new_thread_2.start()
        new_thread_2.join()

    new_thread_4 = threading.Thread(target=task_new, args=('Задача 3',))
    new_thread_4.start()

    new_thread_3 = threading.Thread(target=task, args=('Задача 3',))
    new_thread_3.start()

    new_thread_3.join()
    new_thread_4.join()

    print('я главный поток, я закончил работу, я домой')


# мультипроцессорность
@decor
def processings():  # 1.10279
    new_process_1 = multiprocessing.Process(target=task, args=('Задача 1',))
    new_process_1.start()

    new_process_2 = multiprocessing.Process(target=task, args=('Задача 2',))
    new_process_2.start()

    new_process_3 = multiprocessing.Process(target=task, args=('Задача 3',))
    new_process_3.start()

    new_process_1.join()
    new_process_2.join()
    new_process_3.join()

    print('я главный поток, я закончил работу, я домой')


# асинхронная
@decor
def asynchronus():
    async def task_generator():
        await asyncio.gather(*[
            task_a(name='Задача 1'),
            task_a(name='Задача 2'),
            task_a(name='Задача 3'),
        ])

    loop = asyncio.get_event_loop()
    loop.run_until_complete(task_generator())


if __name__ == "__main__":
    # synhronus()    # 3.016   1 процесс и 1 поток, но блокирующие
    # threadings()   # 1.015   1 процесс и много потоков
    # processings()  # 1.102   много процессов и 1 поток (на самом деле много)
    # asynchronus()    # 1.003   1 процесс и 1 поток, но не блокирующие

    # # *(12, 15, 6,) - tuple(кортеж) \ **{"name": "Py", 'age': 12} - dict(словарь)

    # tup1 = (12, 15, 6,)
    # print(*tup1)

    def tas(name, age):
        print(name, age)

    dict1 = {"name": "Py", 'age': 12}
    # tas(name=dict1["name"], age=dict1['age'])
    tas(**dict1)
    # print(name="Py", age=12) # **dict1
