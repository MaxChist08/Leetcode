def remove_duplicates(nums):
    ind1 = 0
    ind2 = 0

    cur = nums[0]
    count_cur = 0

    while ind1 < len(nums):
        if nums[ind1] == cur:
            count_cur += 1
        else:
            cur = nums[ind1]
            count_cur = 1

        if count_cur < 3:
            nums[ind2] = cur
            ind2 += 1
        ind1 += 1

    for i in range(len(nums) - 1, ind2 - 1, -1):
        nums.pop(i)

