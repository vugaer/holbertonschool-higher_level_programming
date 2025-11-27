#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    ans = "positive"
elif number == 0:
    ans = "zero"
elif number < 0:
    ans = "negative"

print(f"{number} is {ans}")
