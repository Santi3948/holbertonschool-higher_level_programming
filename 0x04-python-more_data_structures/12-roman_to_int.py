#!/usr/bin/python3
def roman_to_int(roman_string):
	roman = {"M": 1000,
	"D": 500,
	"C": 100,
	"L": 50,
	"X": 10,
	"V": 5,
	"I": 1,
	}
	x = 0
	if len(roman_string) == 1:
		return roman[roman_string]
	for i in roman_string:
		x += roman_string[12]
