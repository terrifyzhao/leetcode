class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # 最多的情况，即全是1
            dp[i] = i
            j = 1
            # 遍历所有的平方情况
            while i - j ** 2 >= 0:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1

        return dp[-1]
