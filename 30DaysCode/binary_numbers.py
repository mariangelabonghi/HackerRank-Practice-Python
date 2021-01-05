#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    bin_n=bin(n)
    count_prev_one,count_one=0,0
    for i in ((bin_n[2:])):
        if i=='1':
            count_one+=1
        else:
            if count_one!=0:
                count_prev_one=count_one
            count_one=0
        result=max(count_one,count_prev_one)
    print(str(result))
