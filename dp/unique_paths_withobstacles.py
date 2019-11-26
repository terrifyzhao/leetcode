class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int


        res[i][j] = res[i-1][j]+res[i][j-1]
        """
        if obstacleGrid[0][0]:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        res = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            if not obstacleGrid[i][0]:
                res[i][0] = 1
            else:
                break
        for i in range(col):
            if not obstacleGrid[0][i]:
                res[0][i] = 1
            else:
                break
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j]:
                    res[i][j] = 0
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[-1][-1]

    def uniquePathsWithObstacles2(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int

        """
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        obstacleGrid[0][0] = 1

        # 如果当前位置是0，前一位置是1，就给当前位置置1，这里的数字表示的是能走的次数，所以obstacleGrid[0][0]需要提前设置为1
        for i in range(1, row):
            obstacleGrid[i][0] = 1 if obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1 else 0

        for i in range(1, col):
            obstacleGrid[0][i] = 1 if obstacleGrid[0][i] == 0 and obstacleGrid[0][i - 1] == 1 else 0

        for i in range(1, row):
            for j in range(1, col):
                # 这里的数字是指是否有障碍
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]


if __name__ == '__main__':
    o = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # o = [[0, 0], [1, 0]]
    # o = [[0, 0], [1, 1], [0, 0]]
    s = Solution().uniquePathsWithObstacles2(o)
    print(s)
