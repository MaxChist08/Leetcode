def find_nth_digit(n):
    k = 0

    while n > 9 * 10 ** k * (k + 1):
        n -= 9 * 10 ** k * (k + 1)
        k += 1

    n -= 1
    num = 10 ** k + n // (k + 1)

    return int(str(num)[n % (k + 1)])


