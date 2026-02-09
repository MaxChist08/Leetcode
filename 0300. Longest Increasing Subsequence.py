def length_of_LIS(nums):
    def bin_search(D, k):
        s = 0
        f = len(D) - 1

        while s <= f:
            m = (s + f) // 2
            if D[m] >= k:
                f = m - 1
            else:
                s = m + 1

        return s

    DP = [1] * len(nums)
    D = [100000] * (len(nums) + 1)

    for i in range(0, len(nums)):
        l = bin_search(D, nums[i])
        D[l] = min(D[l], nums[i])
        DP[i] = l + 1

    return max(DP)