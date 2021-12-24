#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    rpt = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            rpt += int(arg)
    print(rpt)
