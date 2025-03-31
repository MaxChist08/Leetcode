def search_matrix(matrix, target):
    flag = False

    if len(matrix[0]) >= len(matrix):
        for i in range(len(matrix)):
            if (matrix[i][0] <= target) and (matrix[i][-1] >= target):
                start = 0
                last = len(matrix[0]) - 1
                while start <= last:
                    middle = (start + last) // 2
                    if matrix[i][middle] <= target:
                        start = middle + 1
                    else:
                        last = middle - 1
                if matrix[i][last] == target:
                    return True
    else:
        for i in range(len(matrix[0])):
            if (matrix[0][i] <= target) and (matrix[-1][i] >= target):
                start = 0
                last = len(matrix) - 1
                while start <= last:
                    middle = (start + last) // 2
                    if matrix[middle][i] <= target:
                        start = middle + 1
                    else:
                        last = middle - 1
                if matrix[last][i] == target:
                    return True

    return False