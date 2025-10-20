def integer_break(n):
    ans = 0

    for i in range(2, n + 1):
        ans1 = 1
        count = i
        temp_n = n
        for j in range(i):
            r = temp_n // count
            count -= 1
            temp_n -= r
            ans1 *= r

        ans = max(ans1, ans)

    return ans