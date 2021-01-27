#!/bin/python3

def dayOfProgrammer(year):
    if year==1918:
        return '26.09.1918'
    else:
        if ((year>=1700 and year<=1917) and year%4==0) or \
        ((year>=1919 and year<=2700) and ((year%400==0) or \
        (year%4==0 and year%100!=0))):
            return '12.09.'+str(year)
        else:
            return '13.09.'+str(year)

if __name__ == '__main__':
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print(result)
