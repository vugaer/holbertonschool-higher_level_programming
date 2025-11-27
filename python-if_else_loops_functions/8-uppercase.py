#!/usr/bin/python3

def uppercase(str):
    for ch in str:
        code = ord(ch)
        if 97 <= code <= 122:        # 'a'..'z'
            code = code - 32         # convert to 'A'..'Z'
        print("{:c}".format(code), end='')
    print()
