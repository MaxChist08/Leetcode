class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)

        a = 0
        d = len(nums) - 1
        ans = []

        while a < len(nums) - 2:
            d = len(nums) - 1
            while a < d - 2:
                b = a + 1
                c = d - 1
                while b < c:
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        b += 1
                        while b < c and nums[b] == nums[b-1]:
                            b += 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] < target:
                        b += 1
                        while b < c and nums[b] == nums[b-1]:
                            b += 1
                    elif nums[a] + nums[b] + nums[c] + nums[d] > target:
                        c -= 1
                        while b < c and nums[c] == nums[c+1]:
                            c-=1
                d -= 1
                while a < d - 2 and nums[d] == nums[d + 1]:
                    d -= 1
            a += 1
            while a < len(nums) - 2 and nums[a] == nums[a - 1]:
                a += 1

        return ans