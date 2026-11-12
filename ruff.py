from functools import wraps

result = []

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

x = [["EVEN" if element % 2 == 0 else "ODD" for element in row] for row in matrix]

print(x)


# writing a decorator function based
def decorator(x: int):
    def outer(func):
        def inner(*args, **kwargs):
            print(f"hello {x}")
            result = func(*args, **kwargs)
            return result

        return inner

    return outer


@decorator(x=1)
def func():
    return 2


print(func())


# decorator classed based


class Decorator:
    def __init__(self, x: int):
        self.x = x

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(self.x)
            return func(*args, **kwargs)

        return wrapper


@Decorator(33)
def hello():
    print(1111)


hello()
