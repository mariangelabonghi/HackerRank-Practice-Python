#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    count_positive=0
    count_zeros=0
    for number in arr:
        if number>0:
            count_positive+=1
        elif number==0:
            count_zeros+=1
    total=len(arr)
    count_negative=total-count_positive-count_zeros
    print ("{0:.6f}\r\n".format(count_positive/total)+"{0:.6f}\r\n".format(count_negative/total)+"{0:.6f}".format(count_zeros/total))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
