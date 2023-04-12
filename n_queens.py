# Given a chess board having 
#  cells, you need to place N queens on the board in such a way that no queen attacks any other queen.

# Input:
# The only line of input consists of a single integer denoting N.

# Output:
# If it is possible to place all the N queens in such a way that no queen attacks another queen, then print N lines having N integers. The integer in 
#  line and 
#  column will denote the cell 
#  of the board and should be 1 if a queen is placed at 
#  otherwise 0. If there are more than way of placing queens print any of them. If it is not possible to place all N queens in the desired way, then print "Not possible" (without quotes).




def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not place_queen(board, 0, N):
        print("Not possible")
        return
    for row in board:
        print(*row)

def place_queen(board, row, N):
    if row == N:
        return True
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            if place_queen(board, row + 1, N):
                return True
            board[row][col] = 0
    return False

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 1:
            return False
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

if __name__ == "__main__":
    N = int(input().strip())
    solve_n_queens(N)