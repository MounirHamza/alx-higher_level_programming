#!/usr/bin/python3
import random
number = random.randint(-10, 10)
x = number
if x < 0:
    print (f'{x} is negative')
elif x == 0:
    print (f'{x} is zero')
else x > 0:
    print (f'{x} is positive')
