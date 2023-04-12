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





def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1, N):
                return True

            board[i][col] = 0

    return False


def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]

    if not solve_n_queens_util(board, 0, N):
        print("Not possible")
        return

    for row in board:
        print(*row)


if __name__ == "__main__":
    N = int(input().strip())
    solve_n_queens(N)
