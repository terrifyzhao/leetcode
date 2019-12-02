class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0]) if row else 0

        # dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        dp = [0 for _ in range(col+1)]
        # 第一个值，可以是0也可以是1，不影响
        prev = 0
        maxlen = 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                # 因为要给dp[j]赋值，会被覆盖，所以提前保存好
                tmp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(int(dp[j]),
                                int(dp[j - 1]),
                                prev) + 1
                    maxlen = max(maxlen, dp[j])
                else:
                    dp[j] = 0
                prev = tmp
        return maxlen * maxlen


if __name__ == '__main__':
    print(Solution().maximalSquare(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
