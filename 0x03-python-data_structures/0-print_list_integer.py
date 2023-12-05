#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
    """This prints all integers of a list"""
    for c in range(len(my_list)):
        print("{:d}".format(my_list[c]))
