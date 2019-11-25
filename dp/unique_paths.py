import numpy as np


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int


        path[i][j] = path[i+1][j]+ path[i][j+1]

        """
        path = np.zeros(shape=(n, m), dtype='int')
        for i in range(m):
            path[0][i] = 1
        for j in range(n):
            path[j][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                path[i][j] = path[i - 1][j] + path[i][j - 1]
        return path[-1][-1]

    def uniquePaths2(self, m, n):
        """
        O(2n)空间复杂度，当前值只和pre的值和cur值前一位的值有关系
        :param m:
        :param n:
        :return:
        """
        cur = [1] * m
        pre = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                cur[j] = cur[j - 1] + pre[j]
            pre = cur
        return cur[-1]

    def uniquePaths3(self, m, n):
        """
        O(n)空间复杂度，cur只用到了前一位的值，pre只用到了除了前一位的值，所以可以合并成一个数组
        :param m:
        :param n:
        :return:
        """
        cur = np.ones(m)
        for i in range(1, n):
            for j in range(1, m):
                cur[j] += cur[j - 1]
        return cur[-1]
