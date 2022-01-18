#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        rpta = a / b
    except:
        rpta = None
    finally:
        print("Inside result: {}".format(rpta))
        return (rpta)
