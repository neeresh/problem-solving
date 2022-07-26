import math
import os
import random
import re
import sys

def staircase(n):
    
    forward_list = list(range(n))
    backward_list = list(range(n)[::-1])
    
    for i, j in zip(forward_list, backward_list):
        print(' '*j + '#'*(i+int(1)))
        
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
