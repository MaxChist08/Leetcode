def find_rotate_steps(ring, key):
    def find_right(ring, index, val):
        s = 0

        while ring[index] != val:
            index += 1
            s += 1
            if index == len(ring):
                index = 0

        return index, s

    def find_left(ring, index, val):
        s = 0

        while ring[index] != val:
            index -= 1
            s += 1
            if index == -1:
                index = len(ring) - 1

        return index, s

    dct = dict()

    index1, s1 = find_right(ring, 0, key[0])
    dct[index1] = s1

    index2, s2 = find_left(ring, 0, key[0])
    if index2 in dct:
        dct[index2] = min(dct[index2], s2)
    else:
        dct[index2] = s2

    for x in key[1:]:
        new_dct = dict()

        for y in dct:
            index1, s1 = find_right(ring, y, x)
            if index1 in new_dct:
                new_dct[index1] = min(new_dct[index1], dct[y] + s1)
            else:
                new_dct[index1] = dct[y] + s1

            index2, s2 = find_left(ring, y, x)
            if index2 in new_dct:
                new_dct[index2] = min(new_dct[index2], dct[y] + s2)
            else:
                new_dct[index2] = dct[y] + s2

        dct = new_dct

    ANS = pow(10, 18)
    for x in dct:
        if dct[x] < ANS:
            ANS = dct[x]

    return ANS + len(key)