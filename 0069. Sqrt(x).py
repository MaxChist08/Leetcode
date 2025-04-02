def my_sqrt(x):
    first = 0
    last = 46341

    while first <= last:
        middle = (first + last) // 2
        if middle * middle <= x:
            first = middle + 1
        else:
            last = middle - 1

    return last