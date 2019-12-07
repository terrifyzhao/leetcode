# k=infinity cooldown
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[1][0], dp[0][1] + prices[1])
        dp[1][1] = max(-prices[0], -prices[1])
        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[-1][0]


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)

        di0, di1 = 0, float('-inf')
        d_pre = 0
        for i in range(n):
            tmp = di0
            di0 = max(di0, di1 + prices[i])
            di1 = max(di1, d_pre - prices[i])
            d_pre = tmp
        return di0
