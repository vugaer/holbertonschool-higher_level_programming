#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    cem = 0
    for i in range(1, len(argv)):
        cem += int(argv[i])
    print(cem)
