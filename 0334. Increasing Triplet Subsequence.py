def increasing_triplet(nums):
    num1 = 2 ** 31
    num2 = 2 ** 31
    num3 = 2 ** 31

    for i in range(len(nums)):
        if num1 >= nums[i]:
            num1 = nums[i]
        elif num2 >= nums[i]:
            num2 = nums[i]
        elif num3 >= nums[i]:
            num3 = nums[i]

    return num3 != 2 ** 31