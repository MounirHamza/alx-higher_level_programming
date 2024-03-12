#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')
if islower('c') == True:
    print('{} => lower'.format('a', 'z'))
else:
    print('{} => upper'.format('a', 'z'))
