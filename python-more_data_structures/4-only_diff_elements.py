#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    intersect = [y for y in set_1 if y in set_2]
    merged = list(set(list(set_1) + list(set_2)))
    emptied = merged[:]
    for i in merged:
        if i in intersect:
            emptied.remove(i)
    return emptied
