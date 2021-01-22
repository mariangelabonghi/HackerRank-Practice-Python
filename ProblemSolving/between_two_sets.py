#!/bin/python3

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    count=0
    def div(x,y):
        if x%y==0:
            return True
        else:
            return False
    for i in range(max(a),min(b)+1):
        if all(div(j,i) for j in b) and all(div(i,j) for j in a):
            count+=1
    return count

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print(total)
