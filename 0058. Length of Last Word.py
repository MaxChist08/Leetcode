def length_of_last_word(s):
    a = len(s) - 1
    ans = 0

    while a >= 0 and s[a] == " ":
        a -= 1

    while a >= 0 and s[a] != " ":
        ans += 1
        a -= 1

    return ans