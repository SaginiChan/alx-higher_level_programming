#!/usr/bin/python3
def search_replace(my_list, search, replace):
    simple_list = list(map(lambda c: replace if c == search else c, my_list))
    return (simple_list)
