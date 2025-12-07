#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    intersect = [y for y in set_1 if y in set_2]
    fineshyt = list(set(list(set_1) + list(set_2)))
    [fineshyt.remove(i) for i in fineshyt if i in intersect]
    return fineshyt
