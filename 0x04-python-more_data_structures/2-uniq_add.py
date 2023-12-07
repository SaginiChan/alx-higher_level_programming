#!/usr/bin/python3
def uniq_add(my_list=[]):
    en_list = set(my_list)
    pop = 0

    for c in en_list:
        pop += c

    return (pop)
