# https://github.com/Polinadavyyy/lab11--PD---AC-
# Partner 1: Polina Davydouskaya
# Partner 2: Alexander Chasko

"""Defines functions used to create a simple calculator."""

import math


def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("Number must be nonnegative")


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise TypeError("Invalid input")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Input error")
    return math.log(b, a)


def exp(a, b):
    return a ** b
