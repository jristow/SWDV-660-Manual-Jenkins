#This file creates a function that will take two numbers, x and y, as input and output if
#x is a multiple of y, that is x = yi for some value i.

def is_multiple(x, y):
    if x % y == 0:
        return True
    else:
        return False