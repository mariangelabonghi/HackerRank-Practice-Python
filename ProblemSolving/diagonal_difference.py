#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    result= 0
    n = len(arr[0])
    for i in range(n):
        result+= +arr[i][i] - arr[i][n-i-1]
    return abs(result)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
