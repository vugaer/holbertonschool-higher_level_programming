#!/usr/bin/python3
def remove_char_at(str, n):
    mystr = ''
    if n < 0:
        return str
    else:
        for i in range(len(str)):
            if i == n:
                pass
            else:
                mystr += str[i]
        return mystr
