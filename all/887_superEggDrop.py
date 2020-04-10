class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int 鸡蛋
        :type N: int 楼层
        :rtype: int
        """
        dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

        m = 0
        # dp[m][K] k个鸡蛋，扔m次，最坏的情况下可以测试几层楼
        while dp[m][K] < N:
            m += 1
            for k in range(1, K+1):
                # dp[m - 1][k] k不变，说明鸡蛋没有碎，扔鸡蛋的次数-1
                # dp[m - 1][k - 1] 鸡蛋碎了，扔的次数-1
                # 1是当前的层
                dp[m][k] = dp[m - 1][k] + dp[m - 1][k - 1] + 1
        return m
