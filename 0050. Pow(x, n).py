def my_pow(x, n):
    def pow(x, n):
        if n == 0:
            return 1
        elif n < 0:
            return pow(1 / x, -n)
        elif n % 2 == 0:
            return pow(x * x, n / 2)
        else:
            return x * pow(x * x, (n - 1) / 2)

    return pow(x, n)