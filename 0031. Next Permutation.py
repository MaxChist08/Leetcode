def next_permutation(nums):
    flag = False
    for i in range(len(nums) - 2, -1, -1):
        minimum = 1e7
        min_index = -1

        for j in range(len(nums) - 1, i, -1):
            if (minimum > nums[j]) and (nums[j] > nums[i]):
                minimum = nums[j]
                min_index = j

        if minimum != 1e7:
            nums[i], nums[min_index] = nums[min_index], nums[i]

            for l in range(1, (len(nums) - i - 1) // 2 + 1):
                nums[i + l], nums[-l] = nums[-l], nums[i + l]

            flag = True
            break

    if not flag:
        for i in range(len(nums) // 2):
            x = nums[i]
            nums[i] = nums[-i - 1]
            nums[-i - 1] = x