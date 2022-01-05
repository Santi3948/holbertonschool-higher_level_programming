#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    x = 0
    aux = []
    for i in roman_string:
        aux.append(roman[i])
    xd = [0]
    xd.extend(aux)
    aux.append(0)
    for j, w in zip(reversed(xd), reversed(aux)):
        if j != 0:
            if j >= w:
                x += j
            else:
                x -= j
    return x
