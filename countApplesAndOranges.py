import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    apple_tree_house_dist = []
    orange_tree_house_dist = []
    
    apple_count = 0
    orange_count = 0
    
    for d in apples:
        apple_tree_house_dist.append(a + d)
    
    for d in oranges:
        orange_tree_house_dist.append(b + d)
    
    for d in apple_tree_house_dist:
        if d >= s and d <= t:
            apple_count = apple_count + 1
    
    for d in orange_tree_house_dist:
        if d >= s and d <= t:
            orange_count = orange_count + 1
    
    print(apple_count)
    print(orange_count)
            
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
