def number_of_arithmetic_slices(nums):
    if len(nums) < 3:
        return 0

    index = 2
    cnt = 2

    ANS = 0

    while index < len(nums):
        if nums[index] - nums[index - 1] == nums[index - 1] - nums[index - 2]:
            cnt = max(3, cnt + 1)
        else:
            if cnt >= 3:
                ANS += (1 + (cnt - 2)) * (cnt - 2) // 2
            cnt = 0
        index += 1

    if cnt >= 3:
        ANS += (1 + (cnt - 2)) * (cnt - 2) // 2

    return ANS