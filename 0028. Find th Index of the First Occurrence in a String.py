def str_str(haystack, needle):
    index = -1

    for i in range(len(haystack) - len(needle) + 1):

        if needle[0] == haystack[i]:
            flag = True

            for j in range(0, len(needle)):
                if haystack[i + j] != needle[j]:
                    flag = False
                    break
            if flag:
                index = i
                break

    return index