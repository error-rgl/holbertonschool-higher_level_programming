#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_dv = []

    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            check_dv.append(True)
        else:
            check_dv.append(False)

    return (check_dv)
