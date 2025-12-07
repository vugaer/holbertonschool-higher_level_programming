#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    newdict = {}
    keys = list(a_dictionary.keys()).sort()
    values = list(a_dictionary.values()).sort()

    for i in range(len(keys)):
        print("{}: {}".format(keys[i], values[i]))
