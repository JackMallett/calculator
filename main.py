import sys
from decimal import *
from typing import List


def docalc(input):
    arg1, arg2 = 0, 0
    f = None
    for x in range(1,len(input)-1):
        if input[x] == '+':
            arg1, arg2 = input[:x], input[x+1:]
            f = lambda a,b: a + b
            break
        if input[x] == '-':
            arg1, arg2 = input[:x], input[x+1:]
            f = lambda a,b: a - b
            break
        if input[x] == '*':
            arg1, arg2 = input[:x], input[x+1:]
            f = lambda a,b: a * b
            break
        if input[x] == '/':
            arg1, arg2 = input[:x], input[x+1:]
            f = lambda a,b: a / b
            break
        if input[x] == '^':
            arg1, arg2 = input[:x], input[x+1:]
            f = lambda a,b: a ** b
            break
    if f == None:
        print('Your input was not understood, please try again')
        return(False, False, f)

    return arg1, arg2, f



def psplitter(args):
    args = args.replace(')(', ')*(')
    spots = []
    for x in range(len(args)-1):
        if args[x+1] == '(' and args[x].isnumeric():
            spots.append(x)
    for x in spots:
        args = args[: x + 1] + '*' + args[x + 1:]

    openers = '('
    closers = ')'
    temp = ''
    stack = []
    output = []
    for x in range(len(args)):
        c = args[x]
        if c == '(':
            stack.append(c)
            continue
        if c == ')':
            if temp != '':
                stack.append(temp)
                temp = ''
            start, end = (len(stack) - 1 - stack[::-1].index('(')), len(stack)
            li = stack[start + 1 : end]
            stack[start] = li
            del stack[start + 1 : end]
        if c == '-' and x < 0 or args[x-1] in '*/+-^(':
            temp = temp + c
            continue
        if c.isnumeric():
            temp = temp + c
            continue
        if c in '*/+-^':
            if temp != '':
                stack.append(temp)
                temp = ''
            stack.append(c)
            continue
    stack.append(temp)
    return stack

def calculator(args):
    for x in range(len(args)):
        if type(args[x]) is list:
            args[x] = calculator(args[x])
    # POWER
    while '^' in args:
        for x in range(1, len(args)-1):
            if args[x] == '*':
                arg1, arg2 = args[x - 1], args[x + 1]
                args[x + 1] = str(Decimal(arg1) ^ Decimal(arg2))
                del args[x - 1 : x + 1] 
                break

    # MULTIPLICATION / DIVISION
    while '*' in args or '/' in args:
        for x in range(1, len(args)-1):
            if args[x] == '*':
                arg1, arg2 = args[x - 1], args[x + 1]
                args[x + 1] = str(Decimal(arg1) * Decimal(arg2))
                del args[x - 1 : x + 1]  
                break
            if args[x] == '/':
                arg1, arg2 = args[x - 1], args[x + 1]
                args[x + 1] = str(Decimal(arg1) / Decimal(arg2))
                del args[x - 1 : x + 1] 
                break      
    
    # ADDITION / SUBTRACION
    while '+' in args or '-' in args:
        for x in range(1, len(args)-1):
            if args[x] == '+':
                arg1, arg2 = args[x - 1], args[x + 1]
                args[x + 1] = str(Decimal(arg1) + Decimal(arg2))
                del args[x - 1 : x + 1] 
                break
            if args[x] == '-':
                arg1, arg2 = args[x - 1], args[x + 1]
                args[x + 1] = str(Decimal(arg1) - Decimal(arg2))
                del args[x - 1 : x + 1]  
                break

    return args[0]

def calculate(x):
    x = x.replace(' ','')
    #check for all numeric characters aside from operators
    t = x
    for i in '*/+-^()':
        t = t.replace(i,'')
    if not t.isnumeric():
        return False

    # checks for double operators (ex: 2*+1)
    for i in range(len(x) - 1):
        if x[i] in '*/+-^' and x[i + 1] in '*/+^':
            print(2)
            return False

    # check that every open parenthesis has a closed parenthesis
    if x.count('(') != x.count(')'):
        print(3)
        return False

    return calculator(psplitter(x))



def main():
    print('Please enter your calculation (or "exit" to exit):')
    while(True):
        calculation = input()

        if calculation.lower() == 'exit': break
        result = calculate(calculation)
        if result is False:
            print('Your input was not understood, please try again')
            continue

        sys.stdout.write('\x1b[1A')     #clears input to print calculation and result on same line
        print(calculation + ' = ' + str(Decimal(result).normalize()))
    print('Exited successfully')



if __name__ == "__main__":
    main()
