# A teacher asks the class to open their books to a page number. 
# A student can either start turning pages from the front of the book or from the back of the book. 
# They always turn pages one at a time. When they open the book, page  is always on the right side:
# When they flip page , they see pages  and . 
# Each page except the last page will always be printed on both sides. 
# The last page may only be printed on the front, given the length of the book. 
# If the book is  pages long, and a student wants to turn to page , what is the minimum number of pages to turn? 
# They can start at the beginning or the end of the book.
# Given  and , find and print the minimum number of pages that must be turned in order to arrive at page .
# Example
# Using the diagram above, if the student wants to get to page , they open the book to page , 
# flip  page and they are on the correct page. If they open the book to the last page, page , 
# they turn  page and are at the correct page. Return .
# Function Description
# Complete the pageCount function in the editor below.
# pageCount has the following parameter(s):
# int n: the number of pages in the book
# int p: the page number to turn to
# Returns
# int: the minimum number of pages to turn
# Input Format
# The first line contains an integer , the number of pages in the book.
# The second line contains an integer, , the page to turn to.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    n = int(n)
    p = int(p)
    if p == 1 or p == n:
        return 0
    if p % 2 == 0:
        return min(p // 2, (n - p) // 2)
    if p % 2 != 0:
        return min((p - 1) // 2, (n - p) // 2)
    if p == n - 1 or p == n - 2:
        return 1
    if p == 2 or p == 3:
        return 1
    if p>3 and p<n-2:
        return 2
     

    



    
    # for i in range(n):
    #     n = int(n)
    #     p = int(p)
    # if p == 1 or p == n:
    #     return 0
    # for i in range(1, n):
    #     if p == i:
    #         if p % 2 == 0:
    #             return p // 2
    #         else:
    #             return (p - 1) // 2
    #     elif p == n - i:
    #         if (n - p) % 2 == 0:
    #             return (n - p) // 2
    #         else:
    #             return (n - p - 1) // 2




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()