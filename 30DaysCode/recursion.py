#!/bin/python3

import math
import os
import random
import re
import sys

def factorial(n):
    factor=1
    for i in range(n):
        j =i+1
        factor *= j
    return factor

if __name__ == '__main__':
    n = int(input())
    result = factorial(n)
    print(str(result) + '\n')
