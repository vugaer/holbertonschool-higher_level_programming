#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        maximum = my_list[0]
        for i in my_list:
            if i > my_list[0]:
                maximum = i
        return i
