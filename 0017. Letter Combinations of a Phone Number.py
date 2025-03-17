"""letters = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

s = input()
r = []

ans = []

def f(s, r, index):
    global ans
    if len(r) == len(s):
        k = ""
        for i in r:
            k+=i
        ans.append(k)
        return
    for i in letters[int(s[index])]:
        r += i
        f(s, r, index + 1)
        r.pop()

f(s, r, 0)
print(ans)"""

