class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * n
        dp[0] = 1
        i1 = 0
        i2 = 0
        i3 = 0
        for i in range(1, n):
            dp[i] = min(dp[i1] * 2, dp[i2] * 3, dp[i3] * 5)
            if dp[i] == dp[i1] * 2:
                i1 += 1
            if dp[i] == dp[i2] * 3:
                i2 += 1
            if dp[i] == dp[i3] * 5:
                i3 += 1
        return dp[-1]
