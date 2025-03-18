def subsets(nums):
    def f(nums, a, lst):
        lst.append(list())
        for x in a:
            lst[-1].append(x)

        if len(nums) == 0:
            return

        for i in range(len(nums)):
            a.append(nums[i])
            f(nums[i + 1:], a, lst)
            a.pop()

    lst = list()
    a = list()

    f(nums, a, lst)

    return lst
