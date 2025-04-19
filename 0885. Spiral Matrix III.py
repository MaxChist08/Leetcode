def spiral_matrix_III(rows, cols, rStart, cStart):
    def check_index(i, j):
        if (i >= 0) and (j >= 0) and (i < rows) and (j < cols):
            return True
        return False

    i = rStart
    j = cStart

    ans = list()
    ans.append([i, j])

    if rows != 1 or cols != 1:
        flag = False

        for k in range(1, (max(rows - rStart - 1, rStart, cols - cStart - 1, cStart) + 1) * 2 + 1, 2):
            r = j
            if flag:
                if check_index(i, 0):
                    flag = False
                    j = 0
                    ans.append([i, j])
                    for l in range(1, min(k + r, cols)):
                        j += 1
                        ans.append([i, j])
                    j = r + k - 1
                else:
                    j += (k - 1)
            else:
                for l in range(1, min(cols - r, k)):
                    j += 1
                    ans.append([i, j])
                j = r + k - 1
            j += 1
            if check_index(i, j):
                ans.append([i, j])
            else:
                flag = True

            r = i
            if flag:
                if check_index(0, j):
                    flag = False
                    i = 0
                    ans.append([i, j])
                    for l in range(1, min(k + r, rows)):
                        i += 1
                        ans.append([i, j])
                    i = r + k - 1
                else:
                    i += (k - 1)
            else:
                for l in range(1, min(rows - r, k)):
                    i += 1
                    ans.append([i, j])
                i = r + k - 1
            i += 1
            if check_index(i, j):
                ans.append([i, j])
            else:
                flag = True

            r = j
            if flag:
                if check_index(i, cols - 1):
                    flag = False
                    j = cols - 1
                    ans.append([i, j])
                    for l in range(1, min(k - (r - cols), cols)):
                        j -= 1
                        ans.append([i, j])
                    j = r - k
                else:
                    j -= k
            else:
                for l in range(1, min(k + 1, r + 1)):
                    j -= 1
                    ans.append([i, j])
                j = r - k
            j -= 1
            if check_index(i, j):
                ans.append([i, j])
            else:
                flag = True

            r = i
            if flag:
                if check_index(rows - 1, j):
                    flag = False
                    i = rows - 1
                    ans.append([i, j])
                    for l in range(1, min(k - (r - rows), rows)):
                        i -= 1
                        ans.append([i, j])
                    i = r - k
                else:
                    i -= k
            else:
                for l in range(1, min(k + 1, r + 1)):
                    i -= 1
                    ans.append([i, j])
                i = r - k
            i -= 1
            if check_index(i, j):
                ans.append([i, j])
            else:
                flag = True

    return ans