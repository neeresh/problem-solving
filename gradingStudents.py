import math
import os
import random
import re
import sys

def gradingStudents(grades):
    
    # print(grades)
    i = 0
    for grade in grades:
        
        num = grade
        
        # Finding the next multiple of 5
        if (grade % 5 != 0) and (grade >= 38):
            
            for _ in range(5):
                num = num + 1
                
                if num % 5 == 0:
                    if (num - grade) < 3:
                        grades[i] = num
                        break
                    else:
                        num = grade
                        break
                
        else:
            pass
            
        i = i + 1
    
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
