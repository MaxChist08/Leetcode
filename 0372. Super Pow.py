def super_pow(a, b):
    ans = 1
    r = a

    for i in range(len(b) - 1, -1, -1):
        ans *= (r ** b[i]) % 1337

        r **= 10
        r %= 1337

        ans %= 1337

    return ans