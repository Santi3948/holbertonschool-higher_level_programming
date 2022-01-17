#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
	DivList = []
	for elem in range(list_length):
		try:
			DivList.append(my_list_1[elem] / my_list_2[elem])
		except ZeroDivisionError:
			print("division by 0")
			DivList.append(0)
		except TypeError:
			print("wrong type")
			DivList.append(0)
		except IndexError:
			print("out of range")
			DivList.append(0)
		finally:
			continue
	return DivList
