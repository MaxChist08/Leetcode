class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        f = -1
        l = -1

        first = 0
        last = len(nums) - 1

        while first <= last:
            middle = (first + last) // 2
            if nums[middle] >= target:
                last = middle - 1
            else:
                first = middle + 1
        l = last

        first = 0
        last = len(nums) - 1

        while first <= last:
            middle = (first + last) // 2
            if nums[middle] <= target:
                first = middle + 1
            else:
                last = middle - 1
        f = first

        if f - l < 2:
            return -1, -1
        else:
            return l + 1, f - 1