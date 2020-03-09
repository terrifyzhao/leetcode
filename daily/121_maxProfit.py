class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        # dp = [[0 for _ in range(2)] for _ in range(n)]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]

        dp_i0 = 0
        dp_i1 = -prices[0]

        for i in range(1, n):
            dp_i0 = max(dp_i0, dp_i1 + prices[i])
            dp_i1 = max(dp_i1, -prices[i])

            # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp_i0
