def generate(numRows):
    dynamic_matrix = []

    for i in range(numRows):
        dynamic_matrix.append(list())
        for j in range(i + 1):
            dynamic_matrix[-1].append(0)
        dynamic_matrix[-1][0] = dynamic_matrix[-1][-1] = 1

    for i in range(2, numRows):
        for j in range(1, len(dynamic_matrix[i]) - 1):
            dynamic_matrix[i][j] = dynamic_matrix[i - 1][j - 1] + dynamic_matrix[i - 1][j]

    return dynamic_matrix