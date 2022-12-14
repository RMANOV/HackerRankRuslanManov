# There is a large pile of socks that must be paired by color.
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# Example
# There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
# Function Description
# Complete the sockMerchant function in the editor below.
# sockMerchant has the following parameter(s):
# int n: the number of socks in the pile
# int ar[n]: the colors of each sock
# Returns
# int: the number of pairs

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    for i in range(n):
        ar[i] = int(ar[i])
    ar.sort()
    count = 0
    i = 0
    while i < n-1:
        if ar[i] == ar[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
