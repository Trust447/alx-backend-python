#!/usr/bin/env python3

'''a type-annotated module'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    """type-annotated function sum_list
    which takes a list input_list of floats
    as argument and returns their sum as a float"""
    summation = 0.0
    for x in input_list:
        summation += x
    return summation


if __name__ =='__main__':
    sum_list = __import__('5-sum_list').sum_list

    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
    print("sum_list(floats) returns {} which is a {}".format(floats_sum, type(floats_sum)))
