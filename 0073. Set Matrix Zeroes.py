def set_zeroes(matrix):
    cord = list()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                cord.append([i, j])

    for i in cord:
        for i1 in range(len(matrix)):
            matrix[i1][i[1]] = 0
        for j1 in range(len(matrix[0])):
            matrix[i[0]][j1] = 0

    return matrix