#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """This finds all multiples of 2 in a list"""
    mult = []
    for c in range(len(my_list)):
        if my_list[c] % 2 == 0:
            mult.append(True)
        else:
            mult.append(False)

    return (mult)
