# Given an array of integers and a positive integer k, 
# determine the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.
# Function Description
# Complete the divisibleSumPairs function in the editor below.
# divisibleSumPairs has the following parameter(s):
# int n: the length of array 
# int ar[n]: an array of integers
# int k: the integer divisor
# Returns
# - int: the number of pairs
# Input Format
# The first line contains  space-separated integers, n and k.
# The second line contains n space-separated integers, each a value of ar[i].

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()