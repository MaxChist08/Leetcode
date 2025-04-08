def solve(board):
    def f(i, j, board1):
        flag = 1
        if i > 0 and board1[i - 1][j] == "O":
            board1[i][j] = "X"
            flag *= int(f(i - 1, j, board1))
        if j > 0 and board1[i][j - 1] == "O":
            board1[i][j] = "X"
            flag *= int(f(i, j - 1, board1))
        if i < len(board1) - 1 and board1[i + 1][j] == "O":
            board1[i][j] = "X"
            flag *= int(f(i + 1, j, board1))
        if j < len(board1[0]) - 1 and board1[i][j + 1] == "O":
            board1[i][j] = "X"
            flag *= int(f(i, j + 1, board1))
        board1[i][j] = "X"

        if i == 0 or j == 0 or i == len(board1) - 1 or j == len(board1[0]) - 1:
            board1[i][j] = "X"
            return False

        if not flag:
            return False
        else:
            return True

    board1 = []
    for k in range(len(board)):
        board1.append(list())
        for l in range(len(board[0])):
            board1[-1].append(board[k][l])

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board1[i][j] == "O":

                flag = f(i, j, board1)

                if flag:
                    f(i, j, board)