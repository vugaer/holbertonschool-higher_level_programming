#!/usr/bin/python3

def best_score(a_dictionary):
    max_val = max(a_dictionary.values())
    if max_val == None:
        return None
    elif max_val:
        for i in a_dictionary:
            if a_dictionary[i] == max_val:
                return i
