def longest_increasing_path(matrix):
    def DFS(matrix, DP, i, j):
        DP[i][j] = 1

        if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
            if DP[i - 1][j] == -1:
                DP[i - 1][j] = DFS(matrix, DP, i - 1, j)
            DP[i][j] = max(DP[i][j], DP[i - 1][j] + 1)
        if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
            if DP[i][j - 1] == -1:
                DP[i][j - 1] = DFS(matrix, DP, i, j - 1)
            DP[i][j] = max(DP[i][j], DP[i][j - 1] + 1)
        if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
            if DP[i + 1][j] == -1:
                DP[i + 1][j] = DFS(matrix, DP, i + 1, j)
            DP[i][j] = max(DP[i][j], DP[i + 1][j] + 1)
        if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
            if DP[i][j + 1] == -1:
                DP[i][j + 1] = DFS(matrix, DP, i, j + 1)
            DP[i][j] = max(DP[i][j], DP[i][j + 1] + 1)

        return DP[i][j]

    n = len(matrix)
    m = len(matrix[0])

    DP = list()
    for i in range(n):
        DP.append(list())
        for j in range(m):
            DP[-1].append(-1)

    for i in range(n):
        for j in range(m):
            if DP[i][j] == -1:
                DFS(matrix, DP, i, j)

    ans = 0
    for i in DP:
        for j in i:
            ans = max(ans, j)

    return ans