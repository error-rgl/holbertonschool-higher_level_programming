#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_digit = int(repr(number)[-1]) * -1
    last_digit = int(repr(number)[-1])
    print("{}".format(last_digit), end='')
    return(last_digit)
