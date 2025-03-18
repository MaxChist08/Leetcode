def spiralOrder(matrix):
    B = []

    h = len(matrix)
    w = len(matrix[0])

    for i in range(min(h, w) // 2 + min(h, w) % 2):
        for j in range(i, w - i):
            B.append(matrix[i][j])
        for j in range(i + 1, h - i):
            B.append(matrix[j][w - i - 1])
        for j in range(w - i - 2, i - 1, -1):
            B.append(matrix[h - i - 1][j])
        for j in range(h - i - 2, i, -1):
            B.append(matrix[j][i])

    return B[:h * w]