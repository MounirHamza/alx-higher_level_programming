def islower(c):
    return ord('a') <= ord(c) <= ord('z')
if islower('c') == True:
    print('{} is lower'.format('a', 'z'))
else:
    print('{} is upper'.format('a', 'z'))
