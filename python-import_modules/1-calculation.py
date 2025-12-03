#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as meagre
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, meagre.add(a, b)))
    print("{} - {} = {}".format(a, b, meagre.sub(a, b)))
    print("{} * {} = {}".format(a, b, meagre.mul(a, b)))
    print("{} / {} = {}".format(a, b, meagre.div(a, b)))
