def min_window(s, t):
    def check_dicts(s_dict, t_dict):
        for x in t_dict:
            if x not in s_dict or s_dict[x] < t_dict[x]:
                return 0
        return 1

    t_dict = dict()

    for x in t:
        if x not in t_dict:
            t_dict[x] = 1
        else:
            t_dict[x] += 1

    s_dict = dict()

    L = -1
    R = -1

    ans = s
    flag = False

    while R < len(s) - 1:
        while R < len(s) - 1 and not check_dicts(s_dict, t_dict):
            R += 1
            if s[R] not in s_dict:
                s_dict[s[R]] = 1
            else:
                s_dict[s[R]] += 1

        while L < R and check_dicts(s_dict, t_dict):
            L += 1
            flag = True
            s_dict[s[L]] -= 1

        if len(ans) > R - L + 1:
            ans = s[L:R + 1]

    if not flag:
        return ""
    return ans