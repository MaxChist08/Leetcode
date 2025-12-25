def max_uncrossed_lines(nums1, nums2):
    DP = list()
    for i in range(len(nums1)):
        DP.append(list())
        for j in range(len(nums2)):
            DP[-1].append(0)

    DP[0][0] = (nums1[0] == nums2[0])

    for i in range(1, len(nums1)):
        DP[i][0] = DP[i - 1][0] or (nums1[i] == nums2[0])

    for i in range(1, len(nums2)):
        DP[0][i] = DP[0][i - 1] or (nums1[0] == nums2[i])

    for i in range(1, len(nums1)):
        for j in range(1, len(nums2)):
            if nums1[i] == nums2[j]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            DP[i][j] = max(DP[i][j], max(DP[i - 1][j], DP[i][j - 1]))

    return int(DP[-1][-1])