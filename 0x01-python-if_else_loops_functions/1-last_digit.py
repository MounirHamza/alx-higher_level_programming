#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_d = str(number)[-1]
else:
    last_d = str(number)[0] + str(number)[-1]
if last_d > '5' and number > 0:
    print(f'Last digit of {number} is {last_d} and is greater than 5')
elif last_d == '0':
    print(f'Last digit of {number} is {last_d} and is 0')
else:
    print(f'Last digit of {number} is {last_d} and is less than 6 and not 0')
