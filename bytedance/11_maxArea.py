class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        start = 0
        end = len(height) - 1
        while start < end:
            if height[start] > height[end]:
                res = max(res, height[end] * (end - start))
                end -= 1
            else:
                res = max(res, height[start] * (end - start))
                start += 1
        return res
