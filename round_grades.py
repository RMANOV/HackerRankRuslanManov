

# HackerLand University has the following grading policy:
# Every student receives a  in the inclusive range from  to 0-100
# Any  less than 40 is a failing grade.
# Sam is a professor at the university and likes to round each student's  according to these rules:
# If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
# Examples

# grade 85 round to  (85 - 84 is less than 3)
# grade 29 do not round (result is less than 40)
# grade 57 do not round (60 - 57 is 3 or higher)
# Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

# Function Description
# Complete the function gradingStudents in the editor below.

# gradingStudents has the following parameter(s):

# int grades[n]: the grades before rounding
# Returns

# int[n]: the grades after rounding as appropriate
# Input Format

# The first line contains a single integer, n , the number of students.
# Each line  of the  subsequent lines contains a single integer.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] >= 38:
            if grades[i] % 5 >= 3:
                grades[i] += 5 - grades[i] % 5
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
