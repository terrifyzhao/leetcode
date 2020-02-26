import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if math.log10(n) / math.log10(3) % 1 == 0:
            return True
        return False


s = Solution()
r = s.isPowerOfThree(243)
print(r)
