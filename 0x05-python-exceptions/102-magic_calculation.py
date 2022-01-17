#!/usr/bin/python3
from sys import stderr


def magic_calculation(a, b):
    x = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise(Exception, "Too far")
            else:
                result += (a ** b) / i
        except:
            x = b + a
            break
    return(x)
