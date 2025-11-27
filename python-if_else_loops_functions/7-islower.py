#!/usr/bin/python3
# print(ord('a'))
# print(ord('z'))
# print(ord('A'))
# print(ord('Z'))

def islower(word):
    if 65 <= ord(word) <= 90:
        return False
    elif 97 <= ord(word) <= 122:
        return True
