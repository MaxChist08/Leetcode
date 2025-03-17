def length_of_the_longest_substring(s):
    d = set()
    i = 0
    r = 0
    ans = 0

    while i < len(s):
        if s[i] not in d:
            d.add(s[i])
            ans = max(ans, len(d))
            i += 1
        else:
            if s[i] in d:
                d.remove(s[r])
                r += 1

    return max(ans, len(d))
