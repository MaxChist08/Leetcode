def search(nums, target):
    n = 0

    if nums[0] > nums[-1]:
        start = 0
        finish = len(nums) - 1

        while start < finish - 1:
            middle = (start + finish) // 2
            if nums[start] > nums[middle]:
                finish = middle
            else:
                start = middle
        nums = nums[finish::] + nums[:finish:]
        n = len(nums) - finish

    start = 0
    finish = len(nums) - 1

    while start <= finish:
        middle = (start + finish) // 2
        if nums[middle] >= target:
            finish = middle - 1
        else:
            start = middle + 1

    if start == len(nums) or start < 0 or nums[start] != target:
        return -1
    else:
        if start - n >= 0:
            return start - n
        else:
            return len(nums) + start - n
