# Context
# Given a 6*6 2D Array, A:
# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
# abc
#  d
# efj
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
# Task
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max_sum = -100
    for i in range(4):
        for j in range(4):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sum > max_sum:
                max_sum = sum
    print(max_sum)
