def Sum_two(nums, target):
    b = {nums[0]: 0}
    for i in range(1, len(nums)):
        if (target - nums[i]) in b:
            return b[target - nums[i]], i
        b[nums[i]] = i

print(Sum_two([3,2,4], 6))

