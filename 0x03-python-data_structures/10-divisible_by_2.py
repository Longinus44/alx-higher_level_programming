#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    result = [num % 2 == 0 for num in my_list]
    return result
