#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ndir = a_dictionary.copy()
    value_keys = list(ndir.keys())

    for c in value_keys:
        ndir[c] *= 2

    return (ndir)
