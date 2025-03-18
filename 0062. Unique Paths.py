def unique_paths(m, n):
    A = list()

    for i in range(m):
        a = [0] * n
        A.append(a)

    for i in range(n):
        A[0][i] = 1

    for i in range(m):
        A[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            A[i][j] = A[i - 1][j] + A[i][j - 1]

    return A[m - 1][n - 1]