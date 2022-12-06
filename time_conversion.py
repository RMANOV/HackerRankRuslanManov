

# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    converted_time = ""
    if s[-2:] == "AM" and s[:2] == "12":
        converted_time = "00" + s[2:-2]
    elif s[-2:] == "AM":
        converted_time = s[:-2]
    elif s[-2:] == "PM" and s[:2] == "12":
        converted_time = s[:-2]
    else:
        converted_time = str(int(s[:2]) + 12) + s[2:-2]
    return converted_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
