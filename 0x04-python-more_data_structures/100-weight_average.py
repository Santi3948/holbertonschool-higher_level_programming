#!/usr/bin/python3
def weight_average(my_list=[]):
    x = 0
    y = 0
    if not my_list:
        return 0
    for elem in my_list:
        x += elem[0] * elem[1]
        y += elem[1]
    return x / y
