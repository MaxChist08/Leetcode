def is_valid(s):
    dictionary = {")": "(", "]": "[", "}": "{"}
    a = []
    flag = True

    for i in range(len(s)):
        if s[i] not in dictionary.keys():
            a.append(s[i])
        elif len(a) != 0 and a[len(a) - 1] == dictionary[s[i]]:
            a.pop()
        else:
            flag = False
            break
    if len(a) == 0:
        return flag
    else:
        return False
