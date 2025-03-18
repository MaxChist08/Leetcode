def combination_sum(candidates, target):
    ANS = list()

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

    return ANS