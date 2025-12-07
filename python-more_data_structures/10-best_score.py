#!/usr/bin/python3

def best_score(a_dictionary):
    holder_best = None
    if a_dictionary == {}:
        return None
    for i in a_dictionary:
        if a_dictionary[i] == max(a_dictionary.values()):
            holder_best = i
    return holder_best
