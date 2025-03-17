class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        divisor1 = abs(divisor)
        dividend1 = abs(dividend)

        if divisor1 > dividend1:
            return 0

        def f(a, n, dividend1, b, ans):

            if dividend1 < b:
                return ans

            while a + a < dividend1:
                a += a
                n += n

            ans += n
            return f(b, 1, dividend1 - a, b, ans)

        ans = f(divisor1, 1, dividend1, divisor1, 0)

        if (divisor < 0 and dividend > 0) or (divisor > 0 and dividend < 0):
            ans = -ans

        if ans < (-2 ** 31):
            return -2 ** 31
        elif ans > (2 ** 31 - 1):
            return 2 ** 31 - 1
        else:
            return ans









