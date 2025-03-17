s = input()
answer = s[0]

for i in range(len(s) - 1):
    for j in range(1, len(s)):
        ss = s[i:i+j +1]
        flag = True
        ss1 = sorted(ss, reverse=True)
        print(ss1)
        if ss == ss[::-1]:
            if len(answer) < len(ss):
                answer = ss

print(answer)