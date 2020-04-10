# 最长公共子序列
def lcs(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    path = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                path[i][j] = 1
            else:
                if dp[i][j - 1] > dp[i - 1][j]:
                    dp[i][j] = dp[i][j - 1]
                    path[i][j] = 2
                else:
                    dp[i][j] = dp[i - 1][j]
                    path[i][j] = 3
    res = []

    def back_track(i, j):
        if i == 0 or j == 0:
            return
        if path[i][j] == 1:
            back_track(i - 1, j - 1)
            res.append(str1[i - 1])
        elif path[i][j] == 2:
            back_track(i, j - 1)
        elif path[i][j] == 3:
            back_track(i - 1, j)

    back_track(l1, l2)
    return res


a = lcs('asdjaskjdl', 'asds')
print(a)


# 最长连续公共子序列
def lccs(str1, str2):
    l1 = len(str1)
    l2 = len(str2)

    max_len = 0
    max_index = 0
    dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # max_len = max(max_len, dp[i][j])
            if dp[i][j] > max_len:
                max_len = dp[i][j]
                max_index = i

    return str1[max_index - max_len:max_index]


a = lccs('asdjaskjdl', 'asdsaaa')
print(a)


# 最大子序和
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    max_num = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])

        max_num = max(dp[i], max_num)
    return max_num


a = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(a)


# 最大上升
def CIS(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = 1
    max_len = 0
    for i in range(1, n):
        max_sub_len = 0
        for j in range(i):
            if nums[i] > nums[j]:
                max_sub_len = max(dp[j], max_sub_len)
        dp[i] = max_sub_len + 1
        max_len = max(dp[i], max_len)
    return max_len


a = CIS([2, 1, 4, 6, 5, 0, 9])
print(a)


# 最大连续上升
def CCIS(nums):
    if not nums:
        return 0
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = 1
    max_len = 0
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            dp[i] = dp[i - 1] + 1
            max_len = max(max_len, dp[i])
        else:
            dp[i] = 1
    return max_len


a = CCIS([2, 1, 4, 6, 5, 0, 9])
print(a)

import math


class Solution(object):

    def maxProfit_inf(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        num_i0 = 0
        num_i1 = -prices[0]
        for price in prices:
            tmp = num_i0
            num_i0 = max(num_i0, num_i1 + price)
            num_i1 = max(num_i1, tmp - price)
        return num_i0

    def maxProfit(self, k, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        if k > n // 2:
            return self.maxProfit_inf(prices)
        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]

        for j in range(k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[-1][k][0]


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        num_i0 = 0
        num_i1 = -float('inf')
        n = len(prices)
        for i in range(n):
            tmp = num_i0
            num_i0 = max(num_i0, num_i1 + prices[i])
            num_i1 = max(num_i1, tmp - prices[i])
        return num_i0
