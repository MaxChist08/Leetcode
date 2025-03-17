def Sum_two(nums, target):
    b = {nums[0]: 0}
    for i in range(1, len(nums)):
        if (target - nums[i]) in b:
            return b[target - nums[i]], i
        b[nums[i]] = i


