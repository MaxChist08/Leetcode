def sort_colors(nums):
    ZEROES = nums.count(0)
    ONES = nums.count(1)
    TWOES = nums.count(2)

    for i in range(ZEROES):
        nums[i] = 0
    for i in range(ONES):
        nums[ZEROES + i] = 1
    for i in range(TWOES):
        nums[ZEROES + ONES + i] = 2