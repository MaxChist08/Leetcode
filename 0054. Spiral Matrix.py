class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """B = []

        h = len(matrix)
        w = len(matrix[0])

        k = 0
        t = 0

        for i in range(min(h, w) // 2):
            t = 0
            for j in range(i, w - i):
                B.append(matrix[i][j])
                t = 1
            for j in range(i + 1, h - i):
                B.append(matrix[j][w - i - 1])
            for j in range(w - i - 2, i - 1, -1):
                B.append(matrix[h - i - 1][j])
            for j in range(h - i - 2, i, -1):
                B.append(matrix[j][i])
                t = 0
            k = i + 1
        if k < w - k and not t:
            for j in range(k, w - k):
                B.append(matrix[k][j])
            if k + 1 < h - k:
                for j in range(k + 1, h - k):
                    B.append(matrix[j][w - k - 1])
                if w - k - 2 > k - 1:
                    for j in range(w - k - 2, k - 1, -1):
                        B.append(matrix[h - k - 1][j])
                    for j in range(h - k - 2, k, -1):
                        B.append(matrix[j][k]) 
        return B"""

        B = []

        h = len(matrix)
        w = len(matrix[0])

        for i in range(min(h, w) // 2 + min(h, w) % 2):
            for j in range(i, w - i):
                B.append(matrix[i][j])
            for j in range(i + 1, h - i):
                B.append(matrix[j][w - i - 1])
            for j in range(w - i - 2, i - 1, -1):
                B.append(matrix[h - i - 1][j])
            for j in range(h - i - 2, i, -1):
                B.append(matrix[j][i])

        return B[:h * w]
