def remove_element(nums, val):
    i = 0

    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            i -= 1
        i += 1

    return len(nums)