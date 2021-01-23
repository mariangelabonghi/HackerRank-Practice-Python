#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    count_highest =0
    count_lowest=0
    max_score=scores[0]
    min_score=scores[0]
    for i in range(1,len(scores)):
        if scores[i] > max_score:
            count_highest +=1
            max_score =scores[i]
        if scores[i] < min_score:
            count_lowest +=1
            min_score=scores[i]
    return count_highest, count_lowest


if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(result)
