def majority_element(nums):
    dct = dict()
    for x in nums:
        if x in dct:
            dct[x] += 1
        else:
            dct[x] = 1

    ans = list()
    for x in dct:
        if dct[x] > len(nums) // 3:
            ans.append(x)

    return ans