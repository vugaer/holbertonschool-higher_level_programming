#!/usr/bin/python3

def islower(word):
    if 65 <= ord(word) <= 90:
        return False
    elif 97 <= ord(word) <= 122:
        return True
    
def make_upper(word):
    return chr(ord(word)-32)
    
def uppercase(anything):
    for i in anything:
        if islower(i):
            print(make_upper(i), end='')
        else:
            print(i, end='')


uppercase('best school IN the world')