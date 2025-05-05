def num_squares(n):
    dynamic_lst = list()
    for i in range(n + 1):
        dynamic_lst.append(i)

    for i in range(2, int(n ** 0.5) + 1):
        for j in range(0, len(dynamic_lst) - i ** 2):
            dynamic_lst[i ** 2 + j] = min(dynamic_lst[i ** 2 + j], dynamic_lst[j] + 1)
    return dynamic_lst[-1]