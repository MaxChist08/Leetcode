def min_cut(s):
    PALINDROMS = list()
    for i in range(len(s)):
        PALINDROMS.append(list())
        for j in range(len(s)):
            PALINDROMS[-1].append(0)

    for i in range(len(s)):
        PALINDROMS[i][i] = 1

    for i in range(0, len(s) - 1):
        if s[i] == s[i + 1]:
            PALINDROMS[i][i + 1] = 1

    for i in range(2, len(s)):
        for j in range(0, len(s) - i):
            if s[j] == s[j + i]:
                PALINDROMS[j][j + i] = PALINDROMS[j + 1][j + i - 1]

    DP = [0] * (len(s) + 1)

    for i in range(1, len(s) + 1):
        DP[i] = DP[i - 1] + 1
        for j in range(i - 1, 0, -1):
            if PALINDROMS[j - 1][i - 1]:
                DP[i] = min(DP[i], DP[j - 1] + 1)

    return DP[-1] - 1