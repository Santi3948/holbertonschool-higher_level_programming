#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        Div = a/b
    except ZeroDivisionError:
        Div = None
    finally:
        print("Inside result: {}" .format(Div))
    return Div
