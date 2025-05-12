def find_anagrams(s, p):
    d_p = dict()
    for i in p:
        if i in d_p:
            d_p[i] += 1
        else:
            d_p[i] = 1

    d_s = dict()
    for i in range(min(len(p), len(s))):
        if s[i] in d_s:
            d_s[s[i]] += 1
        else:
            d_s[s[i]] = 1

    ans = []

    if d_s == d_p:
        ans.append(0)

    for i in range(1, len(s) - len(p) + 1):
        d_s[s[i - 1]] -= 1
        if d_s[s[i - 1]] == 0:
            del d_s[s[i - 1]]

        if s[i + len(p) - 1] in d_s:
            d_s[s[i + len(p) - 1]] += 1
        else:
            d_s[s[i + len(p) - 1]] = 1

        if d_s == d_p:
            ans.append(i)

    return ans