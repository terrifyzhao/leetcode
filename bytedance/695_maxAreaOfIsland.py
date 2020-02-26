class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        column = len(grid[0])

        def dfs(i, j):
            if i >= row or j >= column or i < 0 or j < 0:
                return 0
            if grid[i][j] == 0:
                return 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                return dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1) + 1

        max_count = 0
        for i in range(row):
            for j in range(column):
                count = dfs(i, j)
                max_count = max(count, max_count)

        return max_count
