#!/bin/python3
def getMoneySpent(keyboards, drives, b):
    buy = [sum([x,y]) for x in keyboards for y in drives if sum([x,y]) <= b]
    if buy == []:
        return -1
    return (max(buy))
    #
if __name__ == '__main__':
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)
    print(moneySpent)
