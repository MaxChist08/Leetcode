class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = True

        for i in range(9):
            a = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in a:
                        a.add(board[i][j])
                    else:
                        flag = False

        for i in range(9):
            a = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] not in a:
                        a.add(board[j][i])
                    else:
                        flag = False

        for x, y in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]:
            a = set()
            for i in range(3):
                for j in range(3):
                    if board[i + x][j + y] != ".":
                        if board[i + x][j + y] not in a:
                            a.add(board[i + x][j + y])
                        else:
                            flag = False

        return flag