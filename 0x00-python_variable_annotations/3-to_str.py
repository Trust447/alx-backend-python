#!/usr/bin/env python3

'''a module that takes a float as argument and returns a string'''


def to_str(n: float) -> str:
    '''A function that returns the string quivalent of any float argument'''
    return str(n)


if __name__ == '__main__':
    to_str = __import__('3-to_str').to_str

    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
