#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    x = my_list[0]
    for i in my_list:
        x = my_list[i] if my_list[i] > x else x
    return x
