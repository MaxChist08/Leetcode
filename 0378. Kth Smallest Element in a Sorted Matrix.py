def kth_smallest(matrix, k):
    def count_smaller_numbers(matrix, n, ans):
        i = len(matrix) - 1
        j = 0

        while True:
            if n < matrix[i][j]:
                if i - 1 >= 0:
                    i -= 1
                else:
                    break
            else:
                ans += i + 1
                if j + 1 < len(matrix[0]):
                    j += 1
                else:
                    break

        return ans

    first = matrix[0][0]
    last = matrix[-1][-1]

    while first <= last:
        middle = (first + last) // 2
        if count_smaller_numbers(matrix, middle, 0) < k:
            first = middle + 1
        else:
            last = middle - 1
    return first
