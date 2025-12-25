def min_cost_tickets(days, costs):
    DP = [0] * (days[-1] + 1)
    DP[days[0]] = min(costs[0], min(costs[1], costs[2]))

    D = set()
    for x in days:
        D.add(x)

    for i in range(days[0] + 1, days[-1] + 1):
        if i in D:
            DP[i] = DP[i - 1] + costs[0]
            if i - 7 > -1:
                DP[i] = min(DP[i], DP[i - 7] + costs[1])
            else:
                DP[i] = min(DP[i], costs[1])
            if i - 30 > -1:
                DP[i] = min(DP[i], DP[i - 30] + costs[2])
            else:
                DP[i] = min(DP[i], costs[2])
        else:
            DP[i] = DP[i - 1]

    return DP[days[-1]]