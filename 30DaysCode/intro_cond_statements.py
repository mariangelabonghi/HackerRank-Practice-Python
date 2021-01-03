#!/bin/python3

import math
import os
import random
import re
import sys
def is_weird_number(n):
    if n >= 1 and n <= 100:
        if (n % 2) != 0:
            print("Weird")
        else:
            if (n % 2) == 0:
                if n >= 2 and n <= 5:
                    print("Not Weird")
                elif n >= 6 and n <= 20:
                    print("Weird")
                elif n > 20:
                   print("Not Weird")

if __name__ == '__main__':
    N = int(input())
    is_weird_number(N)
