#!/usr/bin/python3

def multiply_by_2(b_dictionary):
    a_dictionary = b_dictionary.copy()
    for i in a_dictionary:
        a_dictionary[i] *= 2
    return a_dictionary
