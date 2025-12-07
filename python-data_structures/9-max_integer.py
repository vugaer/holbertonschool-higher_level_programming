#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        maximum = my_list[0]
        for nums in my_list:
            if nums > maximum:
                maximum = nums
        return maximum
