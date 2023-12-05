#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """This finds the biggest integer of a list"""
    if len(my_list) == 0:
        return (None)

    pop = my_list[0]
    for c in range(len(my_list)):
        if my_list[c] > pop:
            pop = my_list[c]

    return (pop)
