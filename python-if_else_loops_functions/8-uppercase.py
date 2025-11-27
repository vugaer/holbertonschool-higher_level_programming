#!/usr/bin/python3

def islower(word):
    if 65 <= ord(word) <= 90:
        return False
    elif 97 <= ord(word) <= 122:
        return True
    else:
         return False
    
def make_upper(word):
    if islower(word):
        return chr(ord(word)-32)
    else:
        return word
    
def uppercase(anything):
    for i in anything:
            print("{}".format(make_upper(i)), end='')

