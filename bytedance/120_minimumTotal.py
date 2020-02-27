class Solution(object):
    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        row = len(triangle)
        dp = [[0 for _ in range(i + 1)] for i in range(row)]
        dp[0][0] = triangle[0][0]

        for i in range(1, row):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        return min(dp[-1])

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        row = len(triangle)
        dp = [0 for _ in range(row)]
        for i in range(row):
            dp[i] = triangle[-1][i]

        for i in range(row - 2, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
