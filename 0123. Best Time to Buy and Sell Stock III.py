def max_profit(prices):
    l = len(prices)

    DP_min = [0] * l
    DP_min[0] = prices[0]

    for i in range(1, l):
        DP_min[i] = min(DP_min[i - 1], prices[i])

    for i in range(l):
        DP_min[i] = prices[i] - DP_min[i]

    for i in range(1, l):
        DP_min[i] = max(DP_min[i - 1], DP_min[i])

    DP_max = [0] * l
    DP_max[l - 1] = prices[l - 1]

    for i in range(l - 2, -1, -1):
        DP_max[i] = max(DP_max[i + 1], prices[i])

    for i in range(l):
        DP_max[i] = DP_max[i] - prices[i]

    for i in range(l - 2, -1, -1):
        DP_max[i] = max(DP_max[i + 1], DP_max[i])

    ANS = 0
    for i in range(l):
        ANS = max(ANS, DP_min[i] + DP_max[i])

    return ANS