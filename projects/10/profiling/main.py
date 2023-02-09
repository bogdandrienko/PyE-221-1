import random
import time
import sys
# import memory_profiler
# mprof run --include-children python main.py
# mprof plot --output memory-profile_good.png


# @memory_profiler.profile
def start():
    car_names = ["Toyota", "Honda", "Audi", "Nissan"]
    car_colors = ["Black", "Blue", "Red", "Yellow", "White"]
    car_count = 10000000

    def create_cars_bad() -> list[dict]:  # carbage collector (Python, Go, C#) (!= C++, Rust, C, Assembler)
        # 8 448 728
        # Elapsed: 10.533797
        cars: list[dict] = []
        for j in range(1, car_count + 1):  # O(N)
            car: dict = {"id": j, "name": random.choice(car_names), "color": random.choice(car_colors)}
            cars.append(car)
        return cars

    def create_cars_good() -> list[dict]:
        # 104 bytes
        # Elapsed: 8.5922858
        for j in range(1, car_count + 1):  # O(N)
            car: dict = {"id": j, "name": random.choice(car_names), "color": random.choice(car_colors)}
            yield car

    _cars = create_cars_bad()  # 8 448 728 / 1024 = 8856
    # _cars = create_cars_good()  # 8 448 728 / 1024 = 8856
    with open("log.txt", "a") as file:
        for i in _cars:
            # print(i["name"])
            file.write(i["name"] + "\n")
            pass
    print(sys.getsizeof(_cars))
    # len(_cars)


if __name__ == "__main__":
    # интерпретация и компиляция(быстрее)
    # https://habr.com/ru/post/417215/
    # наличие или отсутствие(быстрее) сборщика мусора  -  утечка памяти
    # a = {"name": "Oython", "age": 80}
    # del a["name"]
    # a = 12
    # b = a
    # del b
    # динамическая или статическая(быстрее) типизация

    t_start: float = time.perf_counter()
    # start()
    t_stop: float = time.perf_counter()
    print("Elapsed: ", round(t_stop - t_start, 7))

    # cars: list[int] = [x for x in range(1, 1000000)]  # 8 448 728
    # new_cars: tuple[int] = tuple(cars)  # 8 000 032
    # new_cars2 = (x for x in range(1, 1000000))  # 104
    # for idx, i in enumerate(new_cars2, 1):
    #     if idx == 100:
    #         return i
    #     print(i)
    # print(sys.getsizeof(new_cars2))

    # dict1 = {"name": "Python"}  # 232
    # print(sys.getsizeof(dict1))

    # int1: int = 12  # 28 bytes
    # float1: float = 12.1235245234356  # 24 bytes
    # str1: str = "12"  # 51 bytes
    # str2: str = "Python"  # 55 bytes
    # print(sys.getsizeof(float1))
