#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    # Write your code here
    count = 0
    start = 0
    org_m = m
    max_length = len(s)
    
    while True:
        if sum(s[start: m]) == d:
            count = count + 1
            
            start = start + 1
            m = m + 1
        else:

            start = start + 1
            m = m + 1
        
        if m == max_length or len(s) == 1:
            
            if sum(s[-org_m:]) == d and len(s) != 1:
                count = count + 1
            
            break
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
