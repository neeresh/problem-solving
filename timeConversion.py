import math
import os
import random
import re
import sys

def timeConversion(s):
    
    s_split = s.split(':')
    
    # print(s_split)
    
    if ('AM' in s) and (int(s_split[0]) == 12):
        s_split[0] = '00'
    elif ('AM' in s) and (int(s_split[0]) <= 12):
        pass
    elif ('PM' in s) and (int(s_split[0]) >= 12):
        pass
    else:
        s_split[0] = str(int(s_split[0]) + 12)
    
    s_split = ':'.join(s_split)
    
    return s_split.replace('AM', '').replace('PM', '')
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
