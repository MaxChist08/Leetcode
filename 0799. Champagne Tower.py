def champagne_tower(poured, query_row, query_glass):
    lst = list()
    for i in range(100):
        lst.append([0] * (i + 1))

    lst[0][0] = poured
    for i in range(99):
        for j in range(i + 1):
            lst[i + 1][j] += max(0, (lst[i][j] - 1) / 2)
            lst[i + 1][j + 1] += max(0, (lst[i][j] - 1) / 2)

    return min(1, lst[query_row][query_glass])