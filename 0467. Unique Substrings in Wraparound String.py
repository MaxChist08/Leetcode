def find_substring_in_wrapround_string(s):
    dct = dict()
    dct[s[-1]] = 1

    lst = [0] * len(s)
    lst[-1] = 1

    for i in range(len(s) - 2, -1, -1):
        if (s[i + 1] == "a" and s[i] == "z") or (ord(s[i + 1]) - ord(s[i]) == 1):
            lst[i] = lst[i + 1] + 1
            if s[i] not in dct:
                dct[s[i]] = lst[i + 1] + 1
            else:
                dct[s[i]] = max(dct[s[i]], lst[i + 1] + 1)
        else:
            lst[i] = 1
            if s[i] not in dct:
                dct[s[i]] = 1

    ANS = 0
    for x in dct:
        ANS += dct[x]

    return ANS