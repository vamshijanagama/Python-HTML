#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] == "": 
            continue
        elif(97 <= ord(s[i][0]) <= 122):
            if s[i][0].islower():
                a = s[i][0].capitalize() + s[i][1:]
                s[i] = a
    return " ".join(s)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
