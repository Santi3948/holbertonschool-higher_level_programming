#!/usr/bin/python3
for i in range(122, 96, -1):
    x = i
    if not i % 2 == 0:
        x = i - 32
    print("{}" .format(chr(x)), end="")
