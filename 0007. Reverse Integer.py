class Solution:
    def reverse(self, x: int) -> int:
        """a = str(x)
        k = True

        if a[0] == '-':
            a = a[:0:-1]
            k = False
        else:
            a = a[::-1]

        if k:
            x = int(a)
        else:
            x = int(a) * -1

        if x < pow(-2, 31) or x > pow(2, 31) - 1:
            return 0
        else:
            return x"""

        a = str(x)
        k = ""

        if a[0] == '-':
            k = '-'
            a = a[1::]

        a = a[::-1]
        x = int(k + a)

        if x < pow(-2, 31) or x > pow(2, 31) - 1:
            return 0
        else:
            return x