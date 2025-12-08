def shortest_palindrome(s):
    for i in range(len(s), 0, -1):
        if s[:i] == s[:i][::-1]:
            s = (s[i:])[::-1] + s
            return s
    return s