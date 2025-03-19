def search_matrix(matrix, target):
    first_y = 0
    last_y = len(matrix) - 1

    while first_y < last_y:
        middle_y = (first_y + last_y) // 2
        if matrix[middle_y][len(matrix[0]) - 1] >= target:
            if last_y == middle_y:
                last_y = middle_y - 1
            else:
                last_y = middle_y
        else:
            if first_y == middle_y:
                first_y = middle_y + 1
            else:
                first_y = middle_y

    first_x = 0
    last_x = len(matrix[0]) - 1

    while first_x <= last_x:
        middle_x = (first_x + last_x) // 2
        if matrix[first_y][middle_x] >= target:
            last_x = middle_x - 1
        else:
            first_x = middle_x + 1

    if first_x >= len(matrix[0]) or last_x < -1 or matrix[first_y][first_x] != target:
        return False
    else:
        return True