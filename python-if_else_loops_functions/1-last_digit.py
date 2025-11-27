#!/usr/bin/python3
import random
sign = ' '
number = random.randint(-10000, 10000)

last = int(str(number)[-1])

if last == 0:
    condition = "0"
elif last < 5 or number < 0:
    condition = "less than 6 and not 0"
    if number < 0:
        sign = " -"
elif last > 5 and number > 0:
    condition = "greater than 5"


print(f"Last digit of {number} is{sign}{last} and is {condition}")