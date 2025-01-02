from os import *
from sys import *
from collections import *
from math import *


def isPossible(arr, n):
    # Write your code here.
    changes = 0
    for i in range(n-1):
       if arr[i] > arr[i+1]:
           changes += 1
           if changes > 1:
               return False
           if i == 0 or arr[i - 1] <= arr[i + 1]:
               arr[i] = arr[i + 1] 
           else:
               arr[i + 1] = arr[i]
    return True
    pass