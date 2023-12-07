#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = sum(x * w for x, w in my_list)
    denominator = sum(w for _, w in my_list)

    return numerator / denominator
