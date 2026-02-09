def find_number_of_LIS(nums):
    DP = [1] * len(nums)
    new_DP = [1] * len(nums)
    ans = 1

    for i in range(1, len(nums)):
        for j in range(i - 1, -1, -1):
            if nums[i] > nums[j]:
                if DP[i] == DP[j] + 1:
                    new_DP[i] += new_DP[j]
                elif DP[i] < DP[j] + 1:
                    new_DP[i] = new_DP[j]
                DP[i] = max(DP[i], DP[j] + 1)

    ANS = 0

    for i in range(len(nums)):
        if DP[i] == max(DP):
            ANS += new_DP[i]

    return ANS