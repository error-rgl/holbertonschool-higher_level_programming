#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        alphab = ord(str[i])
        if alphab >= 97 and alphab <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(alphab - num), end='')
    print()
