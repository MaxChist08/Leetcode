def min_path_sum(grid):
    dynamic_matrix = []
    for i in range(len(grid)):
        dynamic_matrix.append(list())
        for j in range(len(grid[0])):
            dynamic_matrix[-1].append(-1)

    dynamic_matrix[0][0] = grid[0][0]

    for i in range(1, len(dynamic_matrix[0])):
        dynamic_matrix[0][i] = dynamic_matrix[0][i - 1] + grid[0][i]

    for i in range(1, len(dynamic_matrix)):
        dynamic_matrix[i][0] = dynamic_matrix[i - 1][0] + grid[i][0]

    for i in range(1, len(dynamic_matrix)):
        for j in range(1, len(dynamic_matrix[0])):
            dynamic_matrix[i][j] = min(dynamic_matrix[i - 1][j], dynamic_matrix[i][j - 1]) + grid[i][j]

    return dynamic_matrix[-1][-1]