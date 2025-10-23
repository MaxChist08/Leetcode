def num_islands(grid):
    def DFS(lst, used, i, j):
        queue = list()
        queue.append((i, j))
        used[i][j] = 1

        while len(queue):
            cur = queue[0]
            queue.pop(0)

            for x in lst[cur[0]][cur[1]]:
                if used[x[0]][x[1]] == 0:
                    queue.append((x[0], x[1]))
                    used[x[0]][x[1]] = 1

        return

    n = len(grid)
    m = len(grid[0])

    lst = list()
    used = list()

    for i in range(n):
        lst.append(list())
        used.append(list())
        for j in range(m):
            lst[-1].append(list())
            used[-1].append(0)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':

                if i - 1 >= 0 and grid[i - 1][j] == '1':
                    lst[i][j].append((i - 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == '1':
                    lst[i][j].append((i, j - 1))
                if i + 1 < n and grid[i + 1][j] == '1':
                    lst[i][j].append((i + 1, j))
                if j + 1 < m and grid[i][j + 1] == '1':
                    lst[i][j].append((i, j + 1))

    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and used[i][j] == 0:
                ans += 1
                DFS(lst, used, i, j)

    return ans