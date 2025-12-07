#!/usr/bin/python3

def best_score(a_dictionary):
    holder_best = None
    keys = a_dictionary.keys()
    if len(keys) > 0:
        for i in a_dictionary:
            if a_dictionary[i] == max(a_dictionary.values()):
                holder_best = i
    return holder_best
