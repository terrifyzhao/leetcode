class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int 鸡蛋
        :type N: int 楼层
        :rtype: int
        """
        dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

        m = 0
        while dp[m][K] < N:
            m += 1
            for k in range(1, K+1):
                dp[m][k] = dp[m - 1][k] + dp[m - 1][k - 1] + 1
        return m
