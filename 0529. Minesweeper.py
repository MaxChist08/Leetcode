def update_board(board, click):
    def count_mine(board, click):
        n = 0
        y = click[0]
        x = click[1]

        if y - 1 > -1 and board[y - 1][x] == "M":
            n += 1
        if y + 1 < len(board) and board[y + 1][x] == "M":
            n += 1
        if x - 1 > -1 and board[y][x - 1] == "M":
            n += 1
        if x + 1 < len(board[0]) and board[y][x + 1] == "M":
            n += 1
        if x + 1 < len(board[0]) and y + 1 < len(board) and board[y + 1][x + 1] == "M":
            n += 1
        if x - 1 > -1 and y + 1 < len(board) and board[y + 1][x - 1] == "M":
            n += 1
        if x + 1 < len(board[0]) and y - 1 > -1 and board[y - 1][x + 1] == "M":
            n += 1
        if x - 1 > -1 and y - 1 > -1 and board[y - 1][x - 1] == "M":
            n += 1
        return n

    def game(board, click):
        y = click[0]
        x = click[1]

        if board[y][x] == "M":
            board[y][x] = "X"
            return

        if count_mine(board, click) != 0:
            board[y][x] = str(count_mine(board, click))
            return

        if count_mine(board, click) == 0:
            board[y][x] = "B"

        if y - 1 > -1 and board[y - 1][x] == "E":
            game(board, [y - 1, x])
        if y + 1 < len(board) and board[y + 1][x] == "E":
            game(board, [y + 1, x])
        if x - 1 > -1 and board[y][x - 1] == "E":
            game(board, [y, x - 1])
        if x + 1 < len(board[0]) and board[y][x + 1] == "E":
            game(board, [y, x + 1])
        if x + 1 < len(board[0]) and y + 1 < len(board) and board[y + 1][x + 1] == "E":
            game(board, [y + 1, x + 1])
        if x - 1 > -1 and y + 1 < len(board) and board[y + 1][x - 1] == "E":
            game(board, [y + 1, x - 1])
        if x + 1 < len(board[0]) and y - 1 > -1 and board[y - 1][x + 1] == "E":
            game(board, [y - 1, x + 1])
        if x - 1 > -1 and y - 1 > -1 and board[y - 1][x - 1] == "E":
            game(board, [y - 1, x - 1])
        return

    game(board, click)

    return board