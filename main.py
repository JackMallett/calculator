import sys
from decimal import *


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
    if f == None:
        print('Your input was not understood, please try again')
        return(False)
    arg1 = Decimal(arg1[1:]) * -1 if arg1[0] == '-' else Decimal(arg1)
    arg2 = Decimal(arg2[1:]) * -1 if arg2[0] == '-' else Decimal(arg2)

    return f(arg1, arg2)



def main():
    print('Please enter your calculation (or "exit" to exit):')
    while(True):
        calcualtion = input()
        if calcualtion.lower() == 'exit': break
        output = docalc(calcualtion.strip((' ')))
        if output is False:
            continue
        sys.stdout.write('\x1b[1A')     #clears input to print calculation and result on same line
        print(calcualtion + ' = ' + str(output.normalize()))
    print('Exited successfully')


if __name__ == "__main__":
    main()