from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    sequenceOfNumbers.sort()
    for i in range(len(sequenceOfNumbers)-2,-1,-1):
        if sequenceOfNumbers[i] < sequenceOfNumbers[-1]:
            return sequenceOfNumbers[i]
    return -1
    pass


# Taking input using fast I/O.
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n

# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
