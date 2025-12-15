def min_sub_array_len(target, nums):
    l = 0
    r = 0

    cur = nums[0]

    ans = float("inf")

    while r < len(nums):
        if cur < target:
            r += 1
            if r < len(nums):
                cur += nums[r]
        elif cur >= target:
            ans = min(ans, r - l + 1)
            cur -= nums[l]
            l += 1

    if ans == float("inf"):
        return 0
    return ans