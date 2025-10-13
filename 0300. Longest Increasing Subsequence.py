def length_Of_LIS(nums):
    DP = [1] * len(nums)
    ans = 1

    for i in range(1, len(nums)):
        for j in range(i - 1, -1, -1):
            if nums[i] > nums[j]:
                DP[i] = max(DP[i], DP[j] + 1)
                ans = max(ans, DP[i])

    return ans