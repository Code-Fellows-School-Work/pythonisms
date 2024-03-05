from functools import wraps
from time import sleep


def delay(func):
    "Add time delay to rendered text"
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)

    return wrapper


def debug(func):
    def wrapper(*args, **kwargs):
        problem = func(*args, **kwargs)
        return "This is the problem " + problem

    return wrapper


# @delay
@debug
def example(text):
    return text


if __name__ == "__main__":
    print(example("Test Decorators"))
