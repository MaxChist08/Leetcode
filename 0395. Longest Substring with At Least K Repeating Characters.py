def longest_substring(s, k):
    def F(s, k):
        if len(s) == 0:
            return 0

        dct = dict()
        for x in s:
            if x in dct:
                dct[x] += 1
            else:
                dct[x] = 1

        for x in dct:
            if dct[x] < k:
                return max(F(y, k) for y in s.split(x))

        return len(s)

    return F(s, k)