#!/usr/bin/python3
def islower(c):
    c = ord(c)
    for alpha in range(97, 123):
        if c is alpha:
            return True
    return False
