def original_digits(s):
    num_dct = {0: [("z", 1), ("e", 1), ("r", 1), ("o", 1)],
               1: [("o", 1), ("n", 1), ("e", 1)],
               2: [("t", 1), ("w", 1), ("o", 1)],
               3: [("t", 1), ("h", 1), ("r", 1), ("e", 2)],
               4: [("f", 1), ("o", 1), ("u", 1), ("r", 1)],
               5: [("f", 1), ("i", 1), ("v", 1), ("e", 1)],
               6: [("s", 1), ("i", 1), ("x", 1)],
               7: [("s", 1), ("e", 2), ("v", 1), ("n", 1)],
               8: [("e", 1), ("i", 1), ("g", 1), ("h", 1), ("t", 1)],
               9: [("n", 2), ("i", 1), ("e", 1)]}

    lst = [(0, "z"), (2, "w"), (8, "g"), (4, "u"), (3, "r"), (1, "o"), (5, "f"), (6, "x"), (7, "v"), (9, "e")]

    dct = dict()
    for x in s:
        if x in dct:
            dct[x] += 1
        else:
            dct[x] = 1

    ANS = ""

    for x in lst:
        if x[1] in dct:
            count = dct[x[1]]
            for y in num_dct[x[0]]:
                if y[0] in dct:
                    dct[y[0]] -= y[1] * count
            ANS += str(x[0]) * count

    return "".join(sorted(ANS))