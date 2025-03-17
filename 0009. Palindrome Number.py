class Solution:
    def isPalindrome(self, x: int) -> bool:
        """flag = True

        for i in range(len(str(x)) // 2):
            if str(x)[i] != str(x)[len(str(x)) - 1- i]:
                flag = False
            if not flag:
                break

        if flag:
            return True
        return False"""

        """a = str(x)[:len(str(x)) // 2 + len(str(x)) % 2]
        b = str(x)[-1:-1 - len(a):-1]

        if a == b:
            return True
        return False"""

        # return str(x) == str(x)[::-1]

        x1 = x
        a = 0

        while x1 > 0:
            a = a * 10 + x1 % 10
            x1 //= 10

        return x == a