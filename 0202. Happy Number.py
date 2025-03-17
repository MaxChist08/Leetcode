class Solution:
    def isHappy(self, n: int) -> bool:
        a = set()
        while n != 1 and (n not in a):
            a.add(n)
            m = 0
            for x in str(n):
                m += (int(x) ** 2)
            n = m

        if n == 1:
            return True
        else:
            return False