from os import *
from sys import *
from collections import *
from math import *

def minimumParentheses(pattern):

    # Write your code here
    openBr = 0
    closeBr = 0
    count = 0
    for i in pattern:
        if i == "(":
            openBr += 1
        else:
            closeBr += 1
        
        if closeBr > openBr:
            count = count + closeBr - openBr
            closeBr = 0
            openBr = 0

    count += openBr - closeBr
    return count            
    
    # Return the minimum number of parentheses required.
    pass

