from functools import wraps
from time import sleep
import time


def delay(func):
    "Adds time delay to rendered text"
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)

    return wrapper


def debug(func):
    "Helps with debugging issues"
    def wrapper(*args, **kwargs):
        problem = func(*args, **kwargs)
        return "This is the problem " + problem

    return wrapper


def execution_time(func):
    "Returns the execution time of a function"
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {function}: {end_time - start_time}")
        return function
    return wrapper


def convert_set(func):
    def wrapper(*args, **kwargs):
        string = func(*args, **kwargs)
        string_set = set(string)
        return string_set
    return wrapper

# @delay
# @debug
# @execution_time
# @convert_set


def example(text):

    return text


if __name__ == "__main__":
    print(example("Test Decorators"))
