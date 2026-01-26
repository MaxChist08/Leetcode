def palindrome_pairs(words):
    def is_palindrom(s):
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True

    dct = dict()
    for i in range(len(words)):
        dct[words[i]] = i

    ANS = set()

    for i in range(len(words)):
        if words[i] == "":
            for j in range(len(words)):
                if j != i and is_palindrom(words[j]):
                    ANS.add((i, j))
                    ANS.add((j, i))
        else:
            for j in range(len(words[i]), 0, -1):
                if words[i][:j:][::-1] in dct and i != dct[words[i][:j:][::-1]] and is_palindrom(words[i][j::]):
                    ANS.add((i, dct[words[i][:j:][::-1]]))
            for j in range(len(words[i])):
                if words[i][j::][::-1] in dct and i != dct[words[i][j::][::-1]] and is_palindrom(words[i][:j:]):
                    ANS.add((dct[words[i][j::][::-1]], i))

    return list(ANS)