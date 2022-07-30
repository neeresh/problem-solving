#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    # 10 5 20 20 4 5 2 25 1
    
    best = 0
    first_value = scores[0]
    min_value = scores[0]
    worst = 0
    
    for i in range(len(scores)):
        
        # Breaking most point records
        if first_value < scores[i]:
            best = best + 1
            first_value = scores[i]
    
        # Breaking least point records
        if min_value > scores[i]:
            worst = worst + 1
            min_value = scores[i]
    
    return [best, worst]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
