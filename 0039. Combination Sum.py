def combination_sum(candidates, target):
    # depth first search
    """ANS = list()

    def f(sum, target, ans, candidates, ANS):
        if sum > target:
            return
        elif sum == target:
            ans = sorted(ans)
            if ans not in ANS:
                ANS.append(ans)
            return
        for x in candidates:
            ans.append(x)
            f(sum + x, target, ans, candidates, ANS)
            ans.pop()
        return

    f(0, target, [], candidates, ANS)
    return ANS"""


    # dynamic proggraming
    """ANS = list()
    
    for i in range(target + 1):
        ANS.append(list())

    ANS[0].append(list())

    for x in candidates:
        for i in range(x, len(ANS)):
            if i - x == 0 or len(ANS[i - x]) != 0:
                for j in range(len(ANS[i - x])):
                    lst = []
                    for y in ANS[i - x][j]:
                        lst.append(y)
                    lst.append(x)
                    ANS[i].append(lst)

    return ANS[-1]"""