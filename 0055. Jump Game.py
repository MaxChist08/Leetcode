def can_jump(nums):
    dp_lst = [0] * len(nums)
    dp_lst[0] = 1

    for i in range(len(nums)):
        if dp_lst[i] == 1:
            for j in range(min(len(nums) - i - 1, nums[i]), 0, -1):
                if dp_lst[i + j] == 1:
                    break
                if i + j == len(nums) - 1:
                    return True
                dp_lst[i + j] = 1

    if len(nums) == 1:
        return True
    return False