def k_inverse_pairs(n, k):
    def NEW_DP(DP, n):
        NEW = [0] * len(DP)
        NEW[0] = DP[0]

        for i in range(1, min(n, len(DP))):
            NEW[i] = (NEW[i - 1] + DP[i]) % (pow(10, 9) + 7)

        for i in range(n, len(DP)):
            if NEW[i - 1] + DP[i] - DP[i - n] != 0:
                NEW[i] = (NEW[i - 1] + DP[i] - DP[i - n]) % (pow(10, 9) + 7)
            else:
                break

        return NEW

    if k == 0:
        return 1

    DP = [0] * (k + 1)
    DP[0] = 1

    for l in range(2, n + 1):
        DP = NEW_DP(DP, l)

    return DP[k]