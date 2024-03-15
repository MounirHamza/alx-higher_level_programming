#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    argument = sys.argv[1:]
    lgth = len(argument)
    if lgth != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)   
    else:
        a = int(argument[0])
        b = int(argument[2])
        oper = argument[1]
        match oper:
            case "+":
                print('{} {} {} = {}'.format(a, oper, b, add(a,b)))
                sys.exit(0)
            case "-":
                print('{} {} {} = {}'.format(a, oper, b, sub(a,b)))
                sys.exit(0)
            case "*":
                print('{} {} {} = {}'.format(a, oper, b, mul(a,b)))
                sys.exit(0)
            case "/":
                print('{} {} {} = {}'.format(a, oper, b, div(a,b)))
                sys.exit(0)
            case _:
                print("Unknown operator. Available operators: +, -, *, and /")
                sys.exit(1)
