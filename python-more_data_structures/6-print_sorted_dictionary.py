#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    newdict = {}
    keys = sorted(list(a_dictionary.keys()))
    values = sorted(list(a_dictionary.values()))

    for i in range(len(keys)):
        print("{}: {}".format(keys[i], values[i]))
