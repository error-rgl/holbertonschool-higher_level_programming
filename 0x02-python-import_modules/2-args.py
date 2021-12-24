#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv)
    if args == 1:
        print("0 arguments.")
    elif args == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(args - 1))
        for i in range(args - 1):
            print("{}: {}".format(i + 1, argv[i + 1]))
