#!/usr/bin/python3
# def add_tuple(tuple_a=(), tuple_b=()):
#     epstein = []
#     for i in range(2):
#         epstein += [tuple_a[i] + tuple_b[i]]
#     return tuple(epstein)

def add_tuple(tuple_a=(), tuple_b=(), num = 2):
    tuple_a = fill_tuple(tuple_a, 2)
    tuple_b = fill_tuple(tuple_b, 2)
    return tuple(list(map(lambda x, y: x + y, tuple_a, tuple_b))[0:num]) # infinite variables!

def fill_tuple(tuple_test, num = 2):
    if len(tuple_test) == num:
        return tuple_test
    elif len(tuple_test) < num:
        ppa = [0 for i in range(num)]
        for i in range(len(tuple_test)):
            if tuple_test[i] == True:
                ppa[i] = tuple_test[i]
    return tuple(ppa)