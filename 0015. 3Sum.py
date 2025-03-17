class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(0, len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            first = i + 1
            last = len(nums) - 1
            while first < last:
                if nums[first] + nums[i] + nums[last] == 0:
                    ans.append([nums[first], nums[i], nums[last]])
                    first += 1
                    while first < last and nums[first] == nums[first-1]:
                        first+=1
                elif nums[first] + nums[i] + nums[last] < 0:
                    first += 1
                    while first < last and nums[first] == nums[first-1]:
                        first+=1
                else:
                    last -= 1
                    while last > first and nums[last] == nums[last+1]:
                        last-=1
        return ans