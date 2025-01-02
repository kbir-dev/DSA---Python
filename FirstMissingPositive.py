from os import *
from sys import *
from collections import *
from math import *

def firstMissing(arr, n):
    # Write your function here.
    positives = set()
    arr.sort()
    min_pos = 1
    for i in range(n):
        if arr[i] > 0:
            positives.add(arr[i])
    for i in range(len(positives)):
        if min_pos in positives:
            min_pos += 1
        else:
            return min_pos
    return min_pos

# Main Code
t=int(input())

for j in range(t):
    n=int(input())
    arr=[int(i) for i in input().split()]
    ans = firstMissing(arr,n)

    print(ans)
