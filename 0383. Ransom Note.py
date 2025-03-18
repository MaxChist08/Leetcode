def can_construct(ransomNote, magazine):
    ransomNote_dict = dict()
    magazine_dict = dict()

    for x in ransomNote:
        if x not in ransomNote_dict:
            ransomNote_dict[x] = 1
        else:
            ransomNote_dict[x] += 1

    for x in magazine:
        if x not in magazine_dict:
            magazine_dict[x] = 1
        else:
            magazine_dict[x] += 1

    ANS = True

    for k in ransomNote_dict.keys():
        if (k not in magazine_dict) or (magazine_dict[k] - ransomNote_dict[k] < 0):
            ANS = False
            break

    return ANS
