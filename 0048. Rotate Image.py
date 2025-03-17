class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        for i in range(len(matrix) // 2):
            i1 = i
            for j in range(i, len(matrix) - i):
                matrix[j][i], matrix[len(matrix) - 1 - i][j] = matrix[len(matrix) - 1 - i][j], matrix[j][i]
                i1 = j

            for j in range(i + 1, len(matrix) - i):
                matrix[i1][j], matrix[len(matrix) - 1 - j][i1] = matrix[len(matrix) - 1 - j][i1], matrix[i1][j]

            for j in range(i1 - 1, 0 + i, -1):
                matrix[j][i1], matrix[len(matrix) - 1 - i1][j] = matrix[len(matrix) - 1 - i1][j], matrix[j][i1]

        return matrix





