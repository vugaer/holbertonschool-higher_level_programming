#!/usr/bin/python3

import calculator_1 as calc
import sys

if __name__ == "__main__":
    args = sys.argv

    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif len(args) == 4:
        a = int(args[1])
        operator = args[2]
        b = int(args[3])
        if operator not in ["+", "-", "*", "/"]:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if operator == "+":
                print(f"{a} + {b} = {calc.add(a, b)}")
            elif operator == "-":
                print(f"{a} - {b} = {calc.sub(a, b)}")
            elif operator == "*":
                print(f"{a} * {b} = {calc.mul(a, b)}")
            elif operator == "/":
                print(f"{a} / {b} = {calc.div(a, b)}")
