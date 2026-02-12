def word_break(s, wordDict):
    DP = [0] * (len(s) + 1)
    DP[0] = 1

    for i in range(1, len(s) + 1):
        for x in wordDict:
            if i - len(x) >= 0 and x == s[i - len(x):i] and DP[i - len(x)]:
                DP[i] = 1

    return bool(DP[-1])