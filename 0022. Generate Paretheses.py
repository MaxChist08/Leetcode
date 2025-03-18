def generate_parenthesis(n):
    def generate(s, a, n, ans):
        if len(s) == n * 2:
            ans.append(s)
            return

        if n * 2 - len(s) > a:
            s = s + "("
            a += 1
            generate(s, a, n, ans)
            s = s[:-1]
            a -= 1

        if a > 0:
            s = s + ")"
            a -= 1
            generate(s, a, n, ans)
            s = s[:-1]
            a += 1
        return

    s = str()
    ans = list()
    generate(s, 0, n, ans)

    return ans

