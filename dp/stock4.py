# k=k
class Solution(object):

    def maxProfit_inf(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp0 = 0
        dp1 = -prices[0]

        for i in range(1, n):
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, dp0 - prices[i])
        return dp0

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        if k > n / 2:
            return self.maxProfit_inf(prices)
        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]
        for j in range(1, k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[-1][-1][0]
