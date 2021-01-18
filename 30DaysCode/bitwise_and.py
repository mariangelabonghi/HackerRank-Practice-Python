#!/bin/python3

import math
import os
import random
import re
import sys

T = int(input().strip())
for _ in range(T):
    n , k = map(int , input().split())
    result=0
    for i in range(1,n-1):
        for j in range(i+1,n):
            if k>i&j>result:
                result=i&j
            if result>k:
                break
    print(result)
