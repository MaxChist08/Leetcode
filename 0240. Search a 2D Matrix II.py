def search_matrix(matrix, target):
    i = len(matrix) - 1
    j = 0

    while True:
        if target == matrix[i][j]:
            return True
        elif target < matrix[i][j]:
            if i > 0:
                i -= 1
            else:
                return False
        else:
            if j < len(matrix[0]) - 1:
                j += 1
            else:
                return False