def roman_to_int(s):
    alphabet = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    integer = alphabet[s[-1]]

    for i in range(len(s) - 2, -1, -1):
        if alphabet[s[i]] >= alphabet[s[i + 1]]:
            integer += alphabet[s[i]]
        else:
            integer -= alphabet[s[i]]

    return integer