#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    tmplist = []
    for i in my_list:
        if i // 2 == i / 2:
            tmplist += [True]
        elif i // 2 != i / 2:
            tmplist += [False]
    return tuple(tmplist)
