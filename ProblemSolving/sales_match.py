#!/bin/python3

def sockMerchant(n, ar):
    count_pair=0
    for color in set(ar):
        i= ar.count(color)
        count_pair+=i//2
    return count_pair
if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
