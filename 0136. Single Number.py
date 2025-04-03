def single_number(nums):
    # with sorted list
    """nums = sorted(nums)

    single_num = -1

    for x in nums:
        if single_num == -1:
            single_num = x
        elif single_num == x:
            single_num = -1

    return single_num"""

    # with set
    """nums_set = set()

    for x in nums:
        if x in nums_set:
            nums_set.remove(x)
        else:
            nums_set.add(x)

    return int(str(nums_set)[1:-1])"""