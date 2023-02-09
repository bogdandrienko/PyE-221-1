import random
import time


def f1():
    list1: list[int] = [x for x in range(1, 100 + 1)]
    print(list1)

    t_start = time.perf_counter()

    for i in list1:  # O(N)      - 0.0004 (1000) | 0.004 (1000) | 0.04 (10000) | 0.4 (100000) | 4.0 (1000000)
        print(i)

    # for i in list1:         # O(N**2) - 0.07 (100) | 7.0 (1000) | 700.0 (10000) | 700.0 (100000) | 70000.0 (1000000)
    #     for j in list1:
    #         print(i, j)

    t_stop = time.perf_counter()
    print("Elaplsed time: ", round(t_stop - t_start, 7))


def sort_bubble(_src: list[int], is_reverse=False) -> list[int]:
    length = len(_src)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if is_reverse:
                if _src[j] < _src[j + 1]:
                    # table = _src[j]
                    # _src[j] = _src[j + 1]
                    # _src[j + 1] = table
                    #
                    # a = 12
                    # b = 13
                    # a, b = b, a
                    _src[j], _src[j + 1] = _src[j + 1], _src[j]
            else:
                if _src[j] > _src[j + 1]:
                    _src[j], _src[j + 1] = _src[j + 1], _src[j]
    return _src


if __name__ == "__main__":
    list1: list[int] = [random.randint(1, 1000) for x in range(1, 100000 + 1)]
    _is_reverse = False

    print("Source list: ", list1)

    t_start = time.perf_counter()

    # print("sort_bubble list: ", sort_bubble(list1, is_reverse=_is_reverse))
    # 0.0006 (100) | 0.060 (1 000) | 6 (10 000) | 600 (100 000)

    print("sorted list: ", sorted(list1, reverse=_is_reverse))  # C
    # 2.17e-05 (100) | 0.001 (1 000) | 0.006 (10 000) | 0.03 (100 000)

    t_stop = time.perf_counter()
    print("Elaplsed time: ", round(t_stop - t_start, 7))
