#!/bin/python3

import math
import os
import random
import re
import sys

from itertools import combinations

def divisibleSumPairs(n, k, ar):
    # Write your code here
    all_combinations = combinations(ar, 2)
    count = 0
    
    for combination in all_combinations:
        if sum(combination) % k == 0:
            count = count + 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
