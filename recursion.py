# Description: Recursive function to calculate factorial of a number
# Today, we are learning about an algorithmic concept called recursion.
# Recursive Method for Calculating Factorial n! = 1/n * (n-1)!
# Function Description
# Complete the factorial function in the editor below. Be sure to use recursion.
# factorial has the following paramter:
# int n: an integer
# Returns
# int: the factorial of
# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.
# Input Format
# A single integer,  (the argument to pass to factorial).
# Constraints
# Your submission must contain a recursive function named factorial.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def factorial(n):
    # Write your code here
    for i in range(1, n):
        n = n * i
    return n


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + "\n")

    fptr.close()
