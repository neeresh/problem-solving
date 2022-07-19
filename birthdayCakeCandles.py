import math
import os
import random
import re
import sys
import statistics

def birthdayCakeCandles(candles):
    
    mode = statistics.mode(candles)
    
    return candles.count(mode)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
