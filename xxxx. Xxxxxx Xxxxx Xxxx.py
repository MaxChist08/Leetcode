columnTitle = input()
n = 0

for i in range(len(columnTitle)):
    n += (ord(columnTitle[i]) - 64) * pow(26, len(columnTitle) - i - 1)

k = 1
s = ""

while n > 26:
    if n % (26 ** k) // (26 ** (k - 1)) == 0:
        s = "Z" + s
        n -= 26 ** k
    else:
        s = chr(ord('A') - 1 + n % (26 ** k) // (26 ** (k - 1))) + s
        n -= n % (26 ** k)
    k += 1

print(s)