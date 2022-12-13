
# Today, we're working with binary numbers.
# Task
# Given a base-10 integer, n, convert it to binary (base-2). 
# Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. 
# When working with different bases, it is common to show the base as a subscript.
# Example
n=125
# The binary representation of  is 1111101. In base 10, there are 5 and 1 consecutive ones in two groups. Print the maximum,5 .
# Input Format
# A single integer, .
# Constraints
# Output Format
# Print a single base- integer that denotes the maximum number of consecutive 's in the binary representation of .

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary = bin(n)
    binary = binary[2:]
    count = 0
    max_count = 0
    for i in binary:
        if i == '1':
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    print(max_count)
