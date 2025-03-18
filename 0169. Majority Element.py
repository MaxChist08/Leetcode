def majority_element(nums):
    ans = 0
    val = 0

    for x in nums:
        if val == 0:
            ans = x
            val = 1
        elif ans == x:
            val += 1
        else:
            val -= 1
    return ans