def word_break(s, wordDict):
    DP = [0] * (len(s) + 1)
    DP[0] = 1

    NEW_DP = []
    for i in range(len(s) + 1):
        NEW_DP.append(list())
    NEW_DP[0] = [""]

    for i in range(1, len(s) + 1):
        for x in wordDict:
            if i - len(x) >= 0 and x == s[i - len(x):i] and DP[i - len(x)]:
                DP[i] = 1
                for y in NEW_DP[i - len(x)]:
                    if y == "":
                        NEW_DP[i].append(x)
                    else:
                        NEW_DP[i].append(y + " " + x)

    return NEW_DP[-1]