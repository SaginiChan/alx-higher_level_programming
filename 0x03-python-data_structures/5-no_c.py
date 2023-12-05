#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """This removes all characters c and C from a string"""
    duplicate = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(duplicate))
