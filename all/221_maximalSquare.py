class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        row = len(matrix)
        column = len(matrix[0])

        max_len = 0

        dp = [[0 for _ in range(column + 1)] for _ in range(row + 1)]

        for i in range(row):
            for j in range(column):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
                    max_len = max(max_len, dp[i+1][j+1])
        return max_len * max_len


print(Solution().maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
