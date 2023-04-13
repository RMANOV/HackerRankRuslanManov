# You are provided an array 
#  of size 
#  that contains non-negative integers. Your task is to determine whether the number that is formed by selecting the last digit of all the N numbers is divisible by 
# .

# Note: View the sample explanation section for more clarification.

# Input format

# First line: A single integer 
#  denoting the size of array 
# Second line: 
#  space-separated integers.
# Output format

# If the number is divisible by 
# , then print 
# . Otherwise, print 
# .

# Constraints

# Sample Input
# 5
# 85 25 65 21 84
# Sample Output
# No
# Time Limit: 1
# Memory Limit: 256
# Source Limit:
# Explanation
# Last digit of 
#  is 
# .
# Last digit of 
#  is 
# .
# Last digit of 
#  is 
# .
# Last digit of 
#  is 
# .
# Last digit of 
#  is 
# .
# Therefore the number formed is 
#  which is not divisible by 


def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    last_digits = [str(x % 10) for x in arr]
    number = int("".join(last_digits))

    if number % 10 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
