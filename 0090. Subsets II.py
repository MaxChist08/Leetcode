from itertools import combinations

def subsets_with_dup(nums):

    nums = sorted(nums)
    set_with_nums = set()
    ans = list()

    for i in range(0, len(nums) + 1):
        temp = list(combinations(nums, i))

        for _ in temp:
            if _ not in set_with_nums:
                set_with_nums.add(_)
                ans.append(list(x for x in _))

    return ans