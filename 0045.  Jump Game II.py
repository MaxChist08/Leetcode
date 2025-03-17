class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = []
        for i in range(len(nums)):
            ans.append(1e7)

        ans[0] = 0

        for i in range(0, len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j < len(ans):
                    ans[i + j] = min(ans[i + j], ans[i] + 1)

        return ans[-1]