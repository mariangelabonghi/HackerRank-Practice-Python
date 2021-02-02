#!/bin/python3

def pageCount(n, p):
    return (int(min((p//2),n//2-p//2)))

if __name__ == '__main__':
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    print(result)
