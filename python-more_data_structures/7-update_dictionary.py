#!/usr/bin/python3

def update_dictionary(b_dictionary, key, value):
    tmpdict = b_dictionary.copy()
    keys = b_dictionary.keys()
    values = b_dictionary.values()

    if key not in keys:
        tmpdict[key] = value
    elif key in keys:
        tmpdict[key] = value
    
    return tmpdict
