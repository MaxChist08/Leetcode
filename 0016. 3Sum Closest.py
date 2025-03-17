class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i in range(0, len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            first = i + 1
            last = len(nums) - 1
            while first < last:
                if nums[first] + nums[i] + nums[last] == target:
                    return target
                elif nums[first] + nums[i] + nums[last] < target:
                    if abs(target - (nums[first] + nums[i] + nums[last])) < abs(target - ans):
                        ans = nums[first] + nums[i] + nums[last]
                    first += 1
                    while first < last and nums[first] == nums[first-1]:
                        first+=1
                else:
                    if abs(target - (nums[first] + nums[i] + nums[last])) < abs(target - ans):
                        ans = nums[first] + nums[i] + nums[last]
                    last -= 1
                    while last > first and nums[last] == nums[last+1]:
                        last-=1
        return ans