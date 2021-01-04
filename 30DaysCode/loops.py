#!/bin/python3

import math
import os
import random
import re
import sys
def mult_tables(n):
    for i in range(10):
            result=n*(i+1)
            print('{} x {} = {}'.format(str(n),str(i+1),str(result)))
if __name__ == '__main__':
    n = int(input())
    mult_tables(n) 
