import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    
    temp_arr = arr.copy()
    results = []
    
    for i in arr:
        temp_arr.remove(i)
        # print(temp_arr, arr)
        results.append(sum(temp_arr))
        
        temp_arr = arr.copy()
    
    # print(results)
    print(min(results), max(results))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
