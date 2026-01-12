def min_steps(n):
    DP = list()
    for i in range(n + 1):
        DP.append(list())
        for j in range(n + 1):
            DP[-1].append(1000)

    DP[1][0] = 0
    DP[1][1] = 1

    for j in range(1, n + 1):
        for i in range(1, n + 1):
            if i + j < n + 1:
                DP[i + j][j] = min(DP[i][j] + 1, DP[i + j][j])
            DP[i][i] = min(DP[i][i], DP[i][j] + 1)

    return min(DP[-1])