#!/usr/bin/python3
import calculator_1 as meagre
a = 10
b = 5
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, meagre.add(a, b)))
    print("{} - {} = {}".format(a, b, meagre.sub(a, b)))
    print("{} * {} = {}".format(a, b, meagre.mul(a, b)))
    print("{} / {} = {}".format(a, b, meagre.div(a, b)))
