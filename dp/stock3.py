# k=2
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n)]
        dp[0][1][1] = -prices[0]
        dp[0][2][1] = -prices[0]

        for i in range(1, n):
            for k in range(1, 3):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[-1][-1][0]


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        dp_i10 = 0
        dp_i11 = -prices[0]
        dp_i20 = 0
        dp_i21 = -prices[0]

        for i in range(1, n):
            dp_i10 = max(dp_i10, dp_i11 + prices[i])
            dp_i11 = max(dp_i11, - prices[i])
            dp_i20 = max(dp_i20, dp_i21 + prices[i])
            dp_i21 = max(dp_i21, dp_i10 - prices[i])
        return dp_i20
