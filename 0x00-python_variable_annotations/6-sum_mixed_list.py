#!/usr/bin/env python3

from typing import List, Union
'''a type-annotated function module'''


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    ''' a type-annotated function sum_mixed_list which
    takes a list mxd_lst of integers and floats and
    returns their sum as a float.'''
    summation = 0.0
    for x in mxd_lst:
        summation += x
    return summation


if __name__ == '__main__':

    sum_mixed_list = __import__('6-sum_mixed_list').sum_mixed_list

    print(sum_mixed_list.__annotations__)
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
