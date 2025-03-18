def my_atoi(s):
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    i = 0
    ans = "0"
    minus = False

    while i < len(s) and s[i] == " ":
        i += 1

    if i < len(s) and s[i] == '-':
        i += 1
        minus = True
    elif i < len(s) and s[i] == '+':
        i += 1
    elif i < len(s) and s[i] in numbers:
        ans += s[i]
        i += 1

    for j in range(i, len(s)):
        if s[j] not in numbers:
            break
        ans += str(s[j])

    if minus:
        if (-1 * (int(ans))) < (-2 ** 31):
            return -2 ** 31
        return -1 * (int(ans))
    else:
        if int(ans) > (2 ** 31 - 1):
            return 2 ** 31 - 1
        return int(ans)