def unique_paths_with_obstacles(obstacleGrid) :
    A = list()

    for i in range(len(obstacleGrid)):
        a = [0] * (len(obstacleGrid[0]))
        A.append(a)

    for i in range(len(obstacleGrid[0])):
        if obstacleGrid[0][i] != 1:
            A[0][i] = 1
        else:
            break

    for i in range(len(obstacleGrid)):
        if obstacleGrid[i][0] != 1:
            A[i][0] = 1
        else:
            break

    for i in range(1, len(obstacleGrid)):
        for j in range(1, len(obstacleGrid[0])):
            if obstacleGrid[i][j] != 1:
                A[i][j] = A[i - 1][j] + A[i][j - 1]

    return A[len(A) - 1][len(A[0]) - 1]