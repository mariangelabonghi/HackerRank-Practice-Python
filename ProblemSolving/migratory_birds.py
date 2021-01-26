#!/bin/python3

def migratoryBirds(arr):
    arr.sort()
    max_count_bird=0
    for a in set(arr):
        if arr.count(a) > max_count_bird:
            max_count_bird=arr.count(a)
            bird=a
    return bird

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    print(result)
