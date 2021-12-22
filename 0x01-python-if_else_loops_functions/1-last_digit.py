#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    convert = number * -1
    last_digit = (convert % 10) * -1
elif number >= 0:
    last_digit = number % 10

if last_digit > 5:
    ms = "and is greater than 5"
elif last_digit == 0:
    ms = "and is 0"
elif last_digit < 6:
    ms = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, last_digit, ms), end=' ')
