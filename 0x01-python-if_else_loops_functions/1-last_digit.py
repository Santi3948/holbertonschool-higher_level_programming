#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = n % 10
print("Last digit of {:d} is {:d} and is " .format(number, last))
if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
elif last < 6 and not last == 0:
    print("less than 6 and not 0")
