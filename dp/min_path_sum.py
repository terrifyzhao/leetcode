class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        # res = [[0 for _ in range(col)] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif i != 0 and j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]

        return grid[-1][-1]


if __name__ == '__main__':
    a = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    s = Solution().minPathSum(a)
    print(s)
