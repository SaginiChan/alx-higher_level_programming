#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    olist = list(a_dictionary.keys())
    olist.sort()
    for c in olist:
        print("{}: {}".format(c, a_dictionary.get(c)))
