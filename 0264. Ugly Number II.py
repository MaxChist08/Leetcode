def nth_ugly_number(n):
    lst = list()

    for i in range(50):
        for j in range(30):
            for k in range(15):
                lst.append(2 ** i * 3 ** j * 5 ** k)

    lst = sorted(lst)

    return lst[n - 1]





