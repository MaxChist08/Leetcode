def max_sub_array(nums):
    dp = 0
    ans = nums[0]

    for i in range(0, len(nums)):
        dp = max(nums[i], dp + nums[i])
        ans = max(ans, dp)

    return ans