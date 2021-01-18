#!/bin/python3

import os
import sys

def timeConversion(s):
    if s[-2:]=='AM':
        s = s.replace('AM','')
        if s[:2] == '12':
            s = s.replace(s[:2],'00')
    if s[-2:]=='PM':
        s = s.replace('PM','')
        if s[:2] != '12':
            s = s.replace(s[:2],str(int(s[:2])+12))
    return s

if __name__ == '__main__':
    s = input()
    print(timeConversion(s))
