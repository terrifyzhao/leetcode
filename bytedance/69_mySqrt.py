class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None
        if x < 2:
            return x
        left = 2
        right = x // 2
        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            if num == x:
                return mid
            elif num > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
