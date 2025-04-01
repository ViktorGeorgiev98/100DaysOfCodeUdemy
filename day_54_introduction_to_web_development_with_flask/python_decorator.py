# how to create python decorators and what are they
# A decorator is a function that takes another function as an argument and extends its behavior without explicitly modifying it.
# Decorators are often used to add functionality to existing functions or methods in a clean and readable way.

import time


def delay_decorator(function):
    """
    A decorator that delays the execution of the wrapped function by 2 seconds.

    Args:
        function (callable): The function to be wrapped and delayed.

    Returns:
        callable: The wrapped function with a 2-second delay applied.
    """

    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greeting():
    print("Greeting")


# Using the decorator directly
# decorated_function = delay_decorator(say_greeting)
decorated_function = delay_decorator(say_greeting)
decorated_function()
