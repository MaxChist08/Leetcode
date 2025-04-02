def plus_one(digits):
    # with using integer
    """num = 0

    for i in range(len(digits)):
        num += digits[i] * (10 ** (len(digits) - i - 1))

    digits.clear()
    num += 1

    while num != 0:
        digits.append(num % 10)
        num //= 10

    digits.reverse()

    return digits"""

    # without using integer
    """i = len(digits) - 1
    flag = True

    while i > -1 and flag:
        if digits[i] + 1 <= 9:
            digits[i] += 1
            flag = False
        else:
            digits[i] = 0
            i -= 1

    if flag:
        digits.insert(0, 1)

    return digits"""