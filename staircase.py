

# Its base and height are both equal to n. 
# It is drawn using # symbols and spaces. 
# The last line is not preceded by any spaces.
# Write a program that prints a staircase of size n.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(1, n+1):
        print(" " * (n-i) + "#" * i)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
