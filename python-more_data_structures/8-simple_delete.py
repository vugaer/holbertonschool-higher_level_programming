#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    empty_dict = {}
    for i in a_dictionary:
        if i != key:
            empty_dict[i] = a_dictionary[i]
    return empty_dict
