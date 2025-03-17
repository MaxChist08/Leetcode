null = None
root = [5,4,8,11,null,13,4,7,2,null,null,null,1]

targetSum = 22

ans = root[0]

a = []
for i in range(len(root)):
    a.append([])

k = 0
for i in range(len(root)):
    if i + 1 + k < len(root) and root[i + 1 + k] != null:
        a[i].append(i + 1 + k)
    if i + 2 + k < len(root) and root[i + 2 + k] != null:
        a[i].append(i + 2 + k)
    k += 1

flag = False
def f(a, ans, b):
    global flag
    for x in a[b]:
        if ans < targetSum:
            ans += root[x]
            if ans == targetSum:
                flag = True
            f(a, ans, x)
            ans -= root[x]
    return flag

print(f(a, ans, 0))


