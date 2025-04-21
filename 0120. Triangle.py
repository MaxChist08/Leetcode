def minimum_total(triangle):
    ans = triangle[0][0]
    flag = True

    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])

            if i == len(triangle) - 1:
                if flag:
                    ans = triangle[i][j]
                    flag = False
                else:
                    ans = min(ans, triangle[i][j])

    return ans