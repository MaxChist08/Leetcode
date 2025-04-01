def remove_duplicates(nums):
    i = 1

    if len(nums) < 2:
        return len(nums)

    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
            i -= 1
        i += 1

    return len(nums)