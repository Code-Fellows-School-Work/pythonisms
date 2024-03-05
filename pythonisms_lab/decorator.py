from functools import wraps
from time import sleep

def delay(func):
    "Add time delay to rendered text"
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)
    
    return wrapper

@delay
def example(text):
    return text
    
if __name__ == "__main__":
    print(example("Test Decorators"))