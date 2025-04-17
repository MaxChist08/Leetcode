def num_magic_squares_inside(grid):
    def check_matrix(grid, i, j):
        s = set()

        for i1 in range(0, 3):
            for j1 in range(0, 3):
                if (grid[i + i1][j + j1] not in s) and (grid[i + i1][j + j1] <= 9) and (grid[i + i1][j + j1] >= 1):
                    s.add(grid[i + i1][j + j1])
                else:
                    return False

        summ = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]

        if (summ == grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]) and (
                summ == grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]) and (
                summ == grid[i][j] + grid[i][j + 1] + grid[i][j + 2]) and (
                summ == grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]) and (
                summ == grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]) and (
                summ == grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]) and (
                summ == grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]):
            return True

        return False

    ans = 0
    for i in range(0, len(grid) - 2):
        for j in range(0, len(grid[0]) - 2):
            print(check_matrix(grid, i, j))
            if check_matrix(grid, i, j):
                ans += 1
    return ans