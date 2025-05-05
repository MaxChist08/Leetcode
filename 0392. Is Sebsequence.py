def is_subsequence(s, t):
    s_index = 0

    for i in range(len(t)):
        if s_index < len(s) and t[i] == s[s_index]:
            s_index += 1

    if s_index == len(s):
        return True
    else:
        return False