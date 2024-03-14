#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argument = sys.argv[1:]
    i = len(argument)
    if i = 0:
        print('{} arguments.\n'.format(i))
    elif i = 1:
        print('{} argument:\n'.format(i))
        print('{}: {}\n'.format(i, argument))
    else:
        for i in range len(argument):
            print('{} arguments:\n'.format(i))
            print('{}: {}\n'.format(i, argument)
