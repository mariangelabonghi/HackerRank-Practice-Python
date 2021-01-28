#!/bin/python3

def bonAppetit(bill, k, b):
    if (sum(bill)-bill[k])/2 == b:
        print("Bon Appetit")
    else:
        print(str(int((b-(sum(bill)-bill[k])/2))))

if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)
