def get_row(rowIndex):
    lst = [1]
    for i in range(rowIndex):
        temp_lst = [0] * (len(lst) + 1)
        temp_lst[0] = temp_lst[-1] = 1
        for j in range(1, len(temp_lst) - 1):
            temp_lst[j] = lst[j] + lst[j - 1]
        lst = temp_lst

    return lst