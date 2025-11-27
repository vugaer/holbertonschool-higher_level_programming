#!/usr/bin/python3


def islower(ch):
    if 65 <= ord(ch) <= 90:
        return False
    elif 97 <= ord(ch) <= 122:
        return True
    else:
        return False


def make_upper(ch):
    if islower(ch):
        return chr(ord(ch) - 32)
    else:
        return ch


def uppercase(text):
    for ch in text:
        print("{}".format(make_upper(ch)), end='')
