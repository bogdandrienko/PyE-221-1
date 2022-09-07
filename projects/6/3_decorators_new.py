def multiply(function):
    def wrapper(*args, **kwargs):
        kwargs["name"] = kwargs["name"] * 2
        # print(args[0]2)
        # args2 = [args[0]2, args[1:]]
        # print(args2)
        print("multiply")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        resp = function(args, kwargs)
        return resp
    return wrapper


# print(10//2)
# print(int(10/2))
def mydecorator_half(function):
    def wrapper(*args, kwargs):
        print("mydecorator_half")
        print("Что то печатает ДО")
        res = function(*args, **kwargs)
        print("Что то печатает ПОСЛЕ")
        res2 = res[len(res) // 2::]
        return res2
    return wrapper


@multiply
@mydecorator_half
def func1(name):
    return f"Hello, everybody!+{name}"


res = func1(name="python")
print(res)
