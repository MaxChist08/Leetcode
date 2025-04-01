def int_to_roman(num):
    alphabet = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

    string = ""

    while num != 0:
        n = num // (10 ** (len(str(num)) - 1))
        if n <= 3:
            for i in range(n):
                string += alphabet[(10 ** (len(str(num)) - 1))]
            num %= (10 ** (len(str(num)) - 1))
        elif (n > 3) and (n < 5):
            for i in range(5 - n):
                string += alphabet[(10 ** (len(str(num)) - 1))]
            string += alphabet[(10 ** (len(str(num)) - 1)) * 5]
            num %= (10 ** (len(str(num)) - 1))
        elif (n >= 5) and (n < 9):
            string += alphabet[(10 ** (len(str(num)) - 1)) * 5]
            for i in range(n - 5):
                string += alphabet[(10 ** (len(str(num)) - 1))]
            num %= (10 ** (len(str(num)) - 1))
        else:
            for i in range(10 - n):
                string += alphabet[(10 ** (len(str(num)) - 1))]
            string += alphabet[(10 ** (len(str(num)) - 1)) * 10]
            num %= (10 ** (len(str(num)) - 1))

    return string


