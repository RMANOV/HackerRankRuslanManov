# Problem
# Roy has N coin boxes numbered from 1 to N.
# Every day he selects two indices [L,R] and adds 1 coin to each coin box starting from L to R (both inclusive).
# He does this for M number of days.

# After M days, Roy has a query: How many coin boxes have atleast X coins.
# He has Q such queries.

# Input:
# First line contains N - number of coin boxes.
# Second line contains M - number of days.
# Each of the next M lines consists of two space separated integers L and R.
# Followed by integer Q - number of queries.
# Each of next Q lines contain a single integer X.

# Output:
# For each query output the result in a new line.

# Constraints:
# 1 ≤ N ≤ 1000000
# 1 ≤ M ≤ 1000000
# 1 ≤ L ≤ R ≤ N
# 1 ≤ Q ≤ 1000000
# 1 ≤ X ≤ N


def main():
    # Read the input
    N = int(input())
    M = int(input())
    LR = [tuple(map(int, input().split())) for _ in range(M)]
    Q = int(input())
    queries = [int(input()) for _ in range(Q)]

    # Initialize the coin boxes
    coin_boxes = [0] * (N + 1)

    # Add coins to the boxes according to L and R
    for L, R in LR:
        coin_boxes[L - 1] += 1
        coin_boxes[R] -= 1

    # Calculate the number of coins in each box
    for i in range(1, N + 1):
        coin_boxes[i] += coin_boxes[i - 1]

    # Count the number of boxes with at least X coins
    count_boxes = [0] * (N + 1)
    for coins in coin_boxes[:-1]:
        count_boxes[coins] += 1

    for i in range(N - 1, 0, -1):
        count_boxes[i] += count_boxes[i + 1]

    # Answer the queries
    for X in queries:
        print(count_boxes[X])


if __name__ == "__main__":
    main()
