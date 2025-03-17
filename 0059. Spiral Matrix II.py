class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        A = []
        for i in range(0, n):
            A.append([0] * n)

        num = 1
        for i in range(n // 2 + n % 2):
            for j in range(i, n - i):
                A[i][j] = num
                num += 1
            for j in range(i + 1, n - i):
                A[j][n - i - 1] = num
                num += 1
            for j in range(n - i - 2, i - 1, -1):
                A[n - i - 1][j] = num
                num += 1
            for j in range(n - i - 2, i, -1):
                A[j][i] = num
                num += 1

        return A