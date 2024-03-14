#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argument = sys.argv[1:]
    i = len(argument)
    if i == 0:
        print('{}'.format(i))
    else:
        res = 0
        for x in range(1, i+1):
            sum = int(sys.argv[x])
            res += sum
        print('{}'.format(res))
