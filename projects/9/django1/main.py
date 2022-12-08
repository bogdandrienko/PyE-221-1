from typing import Union

a = input("12")
print(a)


def sum1(a: Union[int, float], b: int | float) -> int | float:
    return a + b


result = sum1(a=12, b=12.0) / 10
print(result)
