# You are required to enter a word that consists of 
#  and 
#  that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if 
# .

# Determine if the entered word is similar to word zoo.

# For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

# Input format

# First line: A word that starts with several Zs and continues by several Os.
# Note: The maximum length of this word must be 
# .
# Output format

# Print Yes if the input word can be considered as the string zoo otherwise, print No.

# Sample Input
# zzzoooooo
# Sample Output
# Yes


def is_similar_to_zoo(word):
    z_count = 0
    o_count = 0

    for char in word:
        if char == 'z':
            z_count += 1
        elif char == 'o':
            o_count += 1
        else:
            return False

    return o_count == 2 * z_count

def main():
    input_word = input().strip()
    if len(input_word) <= 20:
        if is_similar_to_zoo(input_word):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()
