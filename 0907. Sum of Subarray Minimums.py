def sum_subarray_mins(arr):
    MOD = int(1e9) + 7

    ANS = 0
    stack = list()
    pref = list()

    for i in range(len(arr)):
        while len(stack) > 0 and arr[stack[-1] - 1] >= arr[i]:
            stack.pop()
            pref.pop()

        stack.append(i + 1)
        if len(pref) == 0:
            pref.append(arr[stack[-1] - 1] * stack[-1])
        else:
            pref.append(pref[-1] + arr[stack[-1] - 1] * (stack[-1] - stack[- 2]))

        ANS += pref[-1]
        ANS %= MOD

    return ANS % MOD