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

        res = row_res.copy()
        for i in range(K):
            for j in range(0, N):
                min_value = row_res[j]
                for k in range(1, N + 1):
                    # 鸡蛋碎了，则从k-1开始，总数+1
                    # max_value = row_res[k - 1] + 1
                    # 如果鸡蛋没碎，就从N-k开始，总数 + 1，并记录最大值
                    # if row_res[N - k] + 1 > max_value:
                    #     max_value = row_res[N - k] + 1
                    max_value = max(row_res[k - 1], row_res[N - k])

                    # 此处是在计算最大步数
                    if max_value < min_value:
                        min_value = max_value
                res[j] = min_value
                row_res = res.copy()

        # 最后位置的值是最优解
        return res[-1]


s = Solution()
result = s.superEggDrop(2, 100)
print(result)
