#!/usr/bin/python3
flag = True
for i in range(ord('z'), ord('a') - 1, -1):
    word = chr(i)
    if flag:
        print(word, end='')
        flag = False
    else:
        print(word.upper(), end='')
        flag = True
