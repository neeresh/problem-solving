import math
import os
import random
import re
import sys

def plusMinus(arr):
    
    positives = 0
    negatives = 0
    zeros = 0
    
    total_len = len(arr)
    
    for i in arr:
        if i < 0:
            negatives = negatives + 1
        elif i > 0:
            positives = positives + 1
        else:
            zeros = zeros + 1
    
    print(round(positives / total_len, 6))
    print(round(negatives / total_len, 6))
    print(round(zeros / total_len, 6))
    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
