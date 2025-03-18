def is_isomorphic(s, t):
    dict_1 = {}
    dict_2 = {}

    for i in range(len(s)):
        if s[i] not in dict_1:
            dict_1[s[i]] = t[i]
        else:
            if dict_1[s[i]] != t[i]:
                return False

        if t[i] not in dict_2:
            dict_2[t[i]] = s[i]
        else:
            if dict_2[t[i]] != s[i]:
                return False

    return True