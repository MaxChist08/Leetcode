def letter_combinations(digits):
    letters = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

    def f(digits, r, index, ans):
        if len(r) == len(digits):
            k = ""
            for i in r:
                k += i
            if len(k) != 0:
                ans.append(k)
            return
        for i in letters[int(digits[index])]:
            r += i
            f(digits, r, index + 1, ans)
            r.pop()

    r = list()
    ans = list()
    f(digits, r, 0, ans)

    return ans