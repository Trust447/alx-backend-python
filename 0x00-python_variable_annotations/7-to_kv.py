#!/usr/bin/env python3

from typing import Tuple, Union

"""type-annotated function module"""



def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''A function that retuns a tuple'''
    return(k, v**2)


if __name__ == '__main__':
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
