def reverse(x):
    a = str(x)
    k = ""
    if a[0] == '-':
        k = '-'
        a = a[1::]

    a = a[::-1]
    x = int(k + a)

    if x < pow(-2, 31) or x > pow(2, 31) - 1:
        return 0
    else:
        return x