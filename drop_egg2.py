# 目标是求最优解的最大次数，即min(max())

class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        row_res = [0] * N
        for i in range(N):
            row_res[i] = i + 1

        for i in range(2, K):
            res = row_res.copy()
            for j in range(1, N):
                # min_value = row_res[j]
                for k in range(1, N):
                    # 鸡蛋碎了，则从k-1开始，总数+1
                    # 如果鸡蛋没碎，就从N-k开始，总数 + 1，并记录最大值
                    row_res[j] = min(row_res[j], 1 + max(res[k - 1], row_res[N - k]))

        return row_res[-1]


s = Solution()
result = s.superEggDrop(2, 100)
print(result)
