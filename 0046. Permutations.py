class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ANS = []

        def f(nums, a, setty, ANS):
            if len(nums) == len(a):
                ANS.append(list())
                for x in a:
                    ANS[-1].append(x)
                return

            for i in range(len(nums)):
                if nums[i] not in setty:
                    setty.add(nums[i])
                    a.append(nums[i])
                    f(nums, a, setty, ANS)
                    setty.remove(nums[i])
                    a.pop()

            return

        a = list()
        setty = set()
        f(nums, a, setty, ANS)

        return ANS