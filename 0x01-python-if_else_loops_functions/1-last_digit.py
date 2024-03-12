#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if str(number)[-1]>'5':
    print(f'{number} and is greater than 5')
elif str(number)[-1]='0':
    print(f'{number} and is zero')
elif str(number)[-1]<6 and!=0:
    print(f'{number} and is less than 6 and not 0')
