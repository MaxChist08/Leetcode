def find_kth_largest(nums, k):
    d = dict()
    for x in nums:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

    for i in range(10 ** 4, -(10 ** 4) - 1, -1):
        if i in d:
            if k > d[i]:
                k -= d[i]
            else:
                return i