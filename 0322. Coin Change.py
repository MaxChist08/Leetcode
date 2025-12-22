def coin_change(coins, amount):
    DP = [100000] * (amount + 1)
    DP[0] = 0

    for i in range(amount + 1):
        for j in range(len(coins)):
            if i - coins[j] > -1 and DP[i - coins[j]] != 100000:
                DP[i] = min(DP[i], DP[i - coins[j]] + 1)

    if DP[amount] == 100000:
        return -1
    return DP[amount]