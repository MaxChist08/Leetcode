def fraction_to_decimal(numerator, denominator):
    dct = dict()

    res = str(abs(numerator) // abs(denominator))
    dct[numerator % denominator] = len(res) + 1

    if numerator * denominator < 0:
        res = '-' + res

    if numerator % denominator != 0:
        res += "."

        numerator = abs(numerator)
        denominator = abs(denominator)

        numerator = (numerator % denominator) * 10

        while len(res) <= 1e5 and numerator != 0:
            if numerator < denominator:
                numerator *= 10
                res += '0'
            else:
                res += str(numerator // denominator)
                if (numerator % denominator) in dct:
                    res1 = res[:dct[numerator % denominator]] + '(' + res[dct[numerator % denominator]:] + ')'
                    return res1
                dct[numerator % denominator] = len(res)
                numerator = (numerator % denominator) * 10

    return res