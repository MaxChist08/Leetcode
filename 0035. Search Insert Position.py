def searchInsert(self, nums: List[int], target: int) -> int:
    first = 0
    last = len(nums) - 1

    while first <= last:
        middle = (first + last) // 2
        if nums[middle] <= target:
            first = middle + 1
        else:
            last = middle - 1

    if nums[last] != target:
        return last + 1
    else:
        return last