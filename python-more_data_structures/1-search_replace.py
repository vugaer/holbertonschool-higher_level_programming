#!/usr/bin/python3

def search_replace(test_list, search, replace):
    my_list = test_list[:]
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
    return my_list
