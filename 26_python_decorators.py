
# Python Decorators

# 1. Simple Decorator
def my_decorator(func):
    def wrapper():
        print("Before Function")
        func()
        print("After Function")
    return wrapper


@my_decorator
def greet():
    print("Hello, Python!")


greet()


# 2. Decorator with Arguments
def message_decorator(func):
    def wrapper(name):
        print("Function Started")
        func(name)
        print("Function Finished")
    return wrapper


@message_decorator
def welcome(name):
    print("Welcome,", name)


welcome("Padmakar")


# 3. Decorator to Calculate Execution Time
import time

def timer_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution Time:", round(end - start, 4), "seconds")
    return wrapper


@timer_decorator
def calculate_sum():
    total = sum(range(100000))
    print("Sum:", total)


calculate_sum()
