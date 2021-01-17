#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    firstName=list()
    for N_itr in range(N):
        firstNameEmailID = input().split()
        emailID = firstNameEmailID[1]
        mailbox = emailID.split("@")
        if mailbox[1]=="gmail.com":
            firstName.append(firstNameEmailID[0])
    firstName.sort()
    for i in firstName:
        print(i,sep="\n")
