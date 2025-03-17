class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [x for x in range(1, n + 1)]

        def f(k, nums, a, ANS):
            if len(a) == k:
                ANS.append(list())
                for x in a:
                    ANS[-1].append(x)
                return

            for i in range(len(nums)):
                a.append(nums[i])
                f(k, nums[i+1::], a, ANS)
                a.pop()

        a = list()
        ANS = list()
        f(k, nums, a, ANS)

        return ANS