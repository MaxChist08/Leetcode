def delete_and_earn(nums):
    lst = [0] * 10002

    for x in nums:
        lst[x] += 1

    DP = [0] * 10002
    DP[0] = 0
    DP[1] = lst[1]

    for i in range(2, 10002):
        DP[i] = max(DP[i - 1], DP[i - 2] + lst[i] * i)

    return DP[-1]