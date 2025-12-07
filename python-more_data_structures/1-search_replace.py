#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
        if my_list[i] == 0:
            my_list[i] == 1
    return my_list
