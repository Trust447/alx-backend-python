#!/usr/bin/env python3

'''A python module that returns the summation of two float numbers'''


def add(a: float, b: float) -> float:
    """function that add that takes a float a and a float
    b as arguments and returns their sum as a float"""
    return a+b


if __name__ == '__main__':
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
