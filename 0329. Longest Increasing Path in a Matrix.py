def longest_increasing_path(matrix):
    def DFS(x, y, DP, matrix):
        for i in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (x + i[0] > -1) and (x + i[0] < len(DP)) and (y + i[1] > -1) and (y + i[1] < len(DP[0])) and matrix[x + i[0]][
                y + i[1]] > matrix[x][y]:
                if DP[x + i[0]][y + i[1]] == 0:
                    DFS(x + i[0], y + i[1], DP, matrix)
                DP[x][y] = max(DP[x][y], DP[x + i[0]][y + i[1]] + 1)

        DP[x][y] = max(DP[x][y], 1)

    n = len(matrix)
    m = len(matrix[0])

    DP = list()
    for i in range(n):
        DP.append(list())
        for j in range(m):
            DP[-1].append(0)

    for i in range(n):
        for j in range(m):
            if DP[i][j] == 0:
                DFS(i, j, DP, matrix)

    return max(max(x) for x in DP)