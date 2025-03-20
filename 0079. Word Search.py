def exist(board, word):
    def find_next(i, j, board1, word, t, flag, board):
        if t == len(word) - 1:
            return True

        if i - 1 >= 0 and board1[i - 1][j] == word[t + 1]:
            t += 1
            board1[i][j] = "-"
            flag = find_next(i - 1, j, board1, word, t, flag, board)
            board1[i][j] = board[i][j]
            t -= 1
        if i + 1 < len(board1) and board1[i + 1][j] == word[t + 1]:
            t += 1
            board1[i][j] = "-"
            flag = find_next(i + 1, j, board1, word, t, flag, board)
            board1[i][j] = board[i][j]
            t -= 1
        if j - 1 >= 0 and board1[i][j - 1] == word[t + 1]:
            t += 1
            board1[i][j] = "-"
            flag = find_next(i, j - 1, board1, word, t, flag, board)
            board1[i][j] = board[i][j]
            t -= 1
        if j + 1 < len(board1[0]) and board1[i][j + 1] == word[t + 1]:
            t += 1
            board1[i][j] = "-"
            flag = find_next(i, j + 1, board1, word, t, flag, board)
            board1[i][j] = board[i][j]
            t -= 1

        return flag

    flag = False
    ans = False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                board1 = list()
                for x in board:
                    board1.append(list())
                    for y in x:
                        board1[-1].append(y)
                ans = find_next(i, j, board1, word, 0, flag, board)
                if ans:
                    return ans
    return ans