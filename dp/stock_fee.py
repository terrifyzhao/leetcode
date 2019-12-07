# k=infinity fee
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]


class Solution2(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][1] = -prices[0]
        di0 = 0
        di1 = -prices[0]

        for i in range(1, n):
            di0 = max(di0, di1 + prices[i] - fee)
            di1 = max(di1, di0 - prices[i])
        return di0
