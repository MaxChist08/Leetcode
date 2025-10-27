def pacific_atlantic(heights):
    def DFS(heights, DP, i, j):
        if i - 1 > -1 and DP[i - 1][j] == 0 and heights[i - 1][j] >= heights[i][j]:
            DP[i - 1][j] = 1
            DFS(heights, DP, i - 1, j)
        if j - 1 > -1 and DP[i][j - 1] == 0 and heights[i][j - 1] >= heights[i][j]:
            DP[i][j - 1] = 1
            DFS(heights, DP, i, j - 1)
        if i + 1 < len(DP) and DP[i + 1][j] == 0 and heights[i + 1][j] >= heights[i][j]:
            DP[i + 1][j] = 1
            DFS(heights, DP, i + 1, j)
        if j + 1 < len(DP[0]) and DP[i][j + 1] == 0 and heights[i][j + 1] >= heights[i][j]:
            DP[i][j + 1] = 1
            DFS(heights, DP, i, j + 1)

    n = len(heights)
    m = len(heights[0])

    DP_PO = list()
    DP_AO = list()

    for i in range(n):
        DP_PO.append([0] * m)
        DP_AO.append([0] * m)

    for i in range(n):
        DP_PO[i][0] = 1
        DFS(heights, DP_PO, i, 0)
        DP_AO[i][-1] = 1
        DFS(heights, DP_AO, i, m - 1)

    for j in range(m):
        DP_PO[0][j] = 1
        DFS(heights, DP_PO, 0, j)
        DP_AO[-1][j] = 1
        DFS(heights, DP_AO, n - 1, j)

    ANS = list()
    for i in range(n):
        for j in range(m):
            if DP_PO[i][j] == DP_AO[i][j] and DP_PO[i][j] == 1:
                ANS.append([i, j])

    return ANS