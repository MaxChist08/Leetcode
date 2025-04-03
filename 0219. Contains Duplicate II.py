def contains_nearby_duplicate(nums, k):
    nums_set = set()
    k = min(k + 1, len(nums))

    for i in range(len(nums)):
        if i >= k:
            nums_set.remove(nums[i - k])
        if nums[i] not in nums_set:
            nums_set.add(nums[i])
        else:
            return True

    return False