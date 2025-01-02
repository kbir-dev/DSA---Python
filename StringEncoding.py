from os import *
from sys import *
from collections import *
from math import *

def encode(message):
    # Write your code here.
    arr = message
    n = len(arr)
    if n == 0:  
        return 
    
    char = arr[0]
    chars = [char]
    counts = []
    l3 = []
    count = 1  

    for i in range(1, n):
        if arr[i] == char:
            count += 1
        else:
            counts.append(count)  
            char = arr[i]         
            chars.append(char)    
            count = 1             

    
    counts.append(count)

    
    for i in range(len(chars)):
        ele = str(chars[i]) + str(counts[i])
        l3.append(ele)

    message = ''.join(l3)
    return message
