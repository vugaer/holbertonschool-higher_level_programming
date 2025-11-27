#!/usr/bin/python3
yurr = ''

def print_last_digit(number):
    global yurr
    if number > 0:
        last = number % 10
    else:
        last = -number % 10
    
    yurr = yurr + str(last)

print(yurr)