class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return []
        n = len(prices)
        # 两种状态，0表示没有持有，1表示持有
        dp = [[0] * 2] * n
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])

        return dp[-1][0]


a = Solution().maxProfit([7, 1, 5, 3, 6, 4])
print(a)
