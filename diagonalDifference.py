import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    primary_diagonal = 0
    
    for i in range(len(arr)):
        primary_diagonal = primary_diagonal + arr[i][i]
    
    secondary_diagonal = 0
    
    for i, j in zip(list(range(len(arr))), list(range(len(arr))[::-1])):
        secondary_diagonal = secondary_diagonal + arr[i][j]
        
    # print(primary_diagonal, secondary_diagonal)
    # print(abs(secondary_diagonal - primary_diagonal))    
        
    return abs(secondary_diagonal - primary_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
