def maximal_square(matrix):
    ans = 0

    dynamic_matrix = list()
    for i in range(len(matrix)):
        dynamic_matrix.append(list())
        for j in range(len(matrix[0])):
            dynamic_matrix[-1].append(0)

    for i in range(0, len(matrix[0])):
        if matrix[0][i] == "1":
            dynamic_matrix[0][i] = 1
            ans = max(ans, 1)

    for i in range(1, len(matrix)):
        if matrix[i][0] == "1":
            dynamic_matrix[i][0] = 1
            ans = max(ans, 1)

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == "1":
                dynamic_matrix[i][j] = 1
                ans = max(ans, 1)
            if dynamic_matrix[i - 1][j - 1] != 0 and dynamic_matrix[i][j - 1] != 0 and dynamic_matrix[i - 1][j] != 0 and \
                    dynamic_matrix[i][j] == 1:
                dynamic_matrix[i][j] = int((min(dynamic_matrix[i - 1][j - 1], dynamic_matrix[i][j - 1],
                                                dynamic_matrix[i - 1][j]) ** 0.5 + 1) ** 2)
                ans = max(ans, dynamic_matrix[i][j])

    return ans
