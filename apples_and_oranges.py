

# The red region denotes the house, where s is the start point, and i is the endpoint. 
# The apple tree is to the left of the house, and the orange tree is to its right.
# Assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.
# When a fruit falls from its tree, it lands  units of distance from its tree of origin along the x-axis. 
# *A negative value of  means the fruit fell x units to the tree's left, and a positive value of x means it falls x units to the tree's right. *
# Function Description
# Complete the countApplesAndOranges function in the editor below. 
# It should print the number of apples and oranges that land on Sam's house, each on a separate line.
# countApplesAndOranges has the following parameter(s):
# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.
# Input Format
# The first line contains two space-separated integers denoting the respective values of s and t.
# The second line contains two space-separated integers denoting the respective values of a and b.
# The third line contains two space-separated integers denoting the respective values of m and n.
# The fourth line contains  space-separated integers denoting the respective distances that each apple falls from point a .
# The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point b.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    for i in range(len(apples)):
        apples[i] = apples[i] + a
    for i in range(len(oranges)):
        oranges[i] = oranges[i] + b
    print(len([i for i in apples if i >= s and i <= t]))
    print(len([i for i in oranges if i >= s and i <= t]))

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
