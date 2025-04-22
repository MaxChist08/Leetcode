def permute_unique(nums):
    def all_permutations(lst, nums, nums1):
        if len(lst) == len_nums:
            ans.append(list())
            for x in lst:
                ans[-1].append(x)
            return
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                lst.append(nums[i])
                all_permutations(lst, nums[:i] + nums[i + 1:], len_nums)
                lst.pop()

    ans = list()

    len_nums = len(nums)
    nums = sorted(nums)

    all_permutations(list(), nums, len_nums)
    return ans
