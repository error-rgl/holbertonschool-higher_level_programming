#!/usr/bin/python3
import random
number = random.randint(-100, 100)

if number < 0:
	last_digit = int(repr(number)[-1]) * -1
elif number >= 0:
	last_digit = int(repr(number)[-1])

print("Last digit of {} is {}".format(number, last_digit), end=' ')

if last_digit > 5:
	print("and is greater than 5")
elif last_digit == 0:
	print("and is 0")
elif last_digit < 6:
	print("and is less than 6 and not 0")

