#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swap = 0
for j in range(n-1):
    for i in range(n-1):
        if a[i]>a[i+1]:
            swap +=1
            a[i],a[i+1] = a[i+1],a[i]
print('Array is sorted in {} swaps.'.format(swap))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))
