class Solution(object):
    # 暴力搜索
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(height)):

            max_left = 0
            max_right = 0
            # 找到左边最高的
            for j in range(i, -1, -1):
                max_left = max(max_left, height[j])
            # 找到右边最高的
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])
            # 取左右的最小者与当前height相减
            res += min(max_left, max_right) - height[i]
        return res

    # 动态规划，提前存储好最高的height
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res
