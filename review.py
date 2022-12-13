
# Given a string, s, of length n that is indexed from 0 to n+1, 
# print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
# Note: 0 is considered to be an even index.

number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    string = input()
    even_string = ""
    odd_string = ""
    for j in range(len(string)):
        if j % 2 == 0:
            even_string += string[j]
        else:
            odd_string += string[j]
    print(even_string, odd_string)

