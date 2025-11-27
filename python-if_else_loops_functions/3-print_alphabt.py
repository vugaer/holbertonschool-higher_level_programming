#!/usr/bin/python3
for alphabet in range(ord('a'), ord('z')+1):
    if chr(alphabet) == "q" or chr(alphabet) == "e":
        pass
    else:
        print('{}'.format(chr(alphabet)), end='')