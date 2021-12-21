#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number >= 0:
    last = number % 10
else:
    last = -number % 10 * -1
print("Last digit of {:d} is {:d} and is".format(number, last), end=' ')
if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
elif last < 6 and not last == 0:
    print("less than 6 and not 0")
