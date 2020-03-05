class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        row = len(grid)
        column = len(grid[0])
        visited = [[0 for _ in range(column)] for _ in range(row)]

        count1 = 0
        bad_oranges = []
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 2:
                    bad_oranges.append([i, j])
                if grid[i][j] == 1:
                    count1 += 1

        # bad_oranges = [[i, j] for j in range(column) for i in range(row) if grid[i][j] == 2]
        time = 0
        while 1:
            new_bad = []
            while bad_oranges:
                ori_x, ori_y = bad_oranges.pop()
                for d in direction:
                    x, y = ori_x + d[0], ori_y + d[1]
                    if 0 <= x < row and 0 <= y < column and visited[x][y] == 0 and grid[x][y] == 1:
                        visited[x][y] = 1
                        grid[x][y] = 2
                        new_bad.append([x, y])
                        count1 -= 1
            if not new_bad:
                break
            bad_oranges = new_bad
            time += 1

        # for i in range(row):
        #     for j in range(column):
        #         if grid[i][j] == 1:
        #             return -1
        if count1 == 0:
            return time
        return -1


a = Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
print(a)

import heapq