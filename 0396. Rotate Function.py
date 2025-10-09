def max_rotate_function(nums):
    ans = 0
    nums_sum = 0

    for i in range(0, len(nums)):
        ans += i * nums[i]
        nums_sum += nums[i]

    temp_ans = ans
    for i in range(len(nums) - 1, -1, -1):
        temp_ans += nums_sum - nums[i] * (len(nums))
        ans = max(ans, temp_ans)

    return ans