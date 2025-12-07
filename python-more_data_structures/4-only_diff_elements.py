#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    newlst = list(set_1+set_2)
    for i in set_1:
        if i in set_2:
            newlst.remove(i)
    return newlst
